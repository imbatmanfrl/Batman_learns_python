from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import logging
from telegram import Update
import re
import json
import asyncio
import os

with open(".env", "r") as file:
    TOKEN = str(file.read())

BOT_USERNAME = "@miniFinanceTrackingBot"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.info("Strating Bot")

user_trackers = {}
from miniPerformanceModel import BudgetModel, WeeksPassed, Calc


def get_user_tracker(user_id):
    if user_id not in user_trackers:
        user_trackers[user_id] = Calc()
    return user_trackers[user_id]

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🏦Welcome to your Friendly Finance tracking bot 🦇

📅SET START DATE 
• /startdate e.g 2025 8 28

💰ADD TODAY'S EARNINGS 
• /earnings e.g 500, 1000, 4000

💸ADD TODAY'S EXPENSES
• /expenses (name & cost e.g Transport 400)

🪙ADD TODAY'S SAVINGS 
• /savings e.g 4556, 8420, 500

💴ADD TODAY'S INVESTMENT 🧧
• /investments (name & cost e.g Equititties😂)

VIEW REPORTS  
• /weekly - This week's summary
• /totals - All-time totals
• /projection  - Project n week(s) ahead

Let's grow and monitor your finances together! 🚀 
""")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"""
📊 Reports
• `/weekly` - This week's earnings vs spending
• `/totals` - All-time totals
• `/projection ` - Forecast n weeks ahead

⚙️ Setup
• `/startdate e.g 2025 8 28` - Set when you started budgeting

💡 Tips
- Use quotes for multi-word items: ` "Phone bill" 100`
- All amounts are in Naira (₦)
👨‍💻 Developer
• /developer - The MAIN MAIN WHO BUILT THIS SHIT BRICK BY BRICK!!
•/support - just in case you feel like donating 
""")


DATE = 1


async def start_date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    await update.message.reply_text("💡 Usage: 2025 8 28 (year month day)")
    return DATE


async def start_date_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date = update.message.text.strip()
    parts = date.split()

    if not all(p.isdigit() for p in parts):
        await update.message.reply_text("💡 Usage: 2025 8 28 (year month day)")

    year, month, day = map(int, parts)
    tracker = get_user_tracker(update.effective_user.id)
    tracker.starting_date(year, month, day)

    await update.message.reply_text(f"""✅ Start Date Set!\n
📅 Started budgeting: {year}-{month:02d}-{day:02d}\n
⏰ You've been budgeting for {getattr(tracker, 'how_long_weeks', 0)} week(s)""")
    return ConversationHandler.END


async def cancelled(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CANCELLED")
    return ConversationHandler.END


conv_handler_date = ConversationHandler(
    entry_points=[CommandHandler("startdate", start_date_command)],
    states={
        DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, start_date_date)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)


AMOUNT = 1


async def earn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    await update.message.reply_text("Please enter an amount ")
    return AMOUNT


async def earn_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    amount = update.message.text.strip()
    parts = amount.split()

    if not all(p.isdigit() for p in parts):
        await update.message.reply_text("please enter numbers not letters")
        return AMOUNT

    amounts = [float(p) for p in parts]
    tracker = get_user_tracker(update.effective_user.id)
    total_earned = tracker.earn_daily(*amounts)
    await update.message.reply_text(f"✅ Added ₦{';'.join(parts)}!\n"
                                    f"💰Total earned today #{total_earned:,.2f}!")


async def cancelled(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CANCELLED")
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("earnings", earn_command)],
    states={
        AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, earn_amount)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

SPEND = 1

async def spent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    await update.message.reply_text(f"enter name of what you spent in and amount (e.g 'food 500') ")
    return SPEND


async def spend_name_and_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    amount = update.message.text.strip().split()

    if not amount[-1].replace(".", "", 1).isdigit():
        await  update.message.reply_text("please enter valid inputs (e.g 'mac book 4000000')")
        return SPEND

    cost = float(amount[-1])
    name = " ".join(amount[:-1])
    tracker = get_user_tracker(update.effective_user.id)
#    total_spent = tracker.spent_today(name, cost)
    tracker.spent_today(name,cost)
    spent_today = getattr(tracker,"total",0)

    await update.message.reply_text(f"✅Added expense to your database! youve earned #{spent_today} so far")

async def cancelled(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CANCELLED")
    return ConversationHandler.END

conv_handler2 = ConversationHandler(
    entry_points=[CommandHandler("expenses", spent_command)],
    states={
        SPEND: [MessageHandler(filters.TEXT & ~filters.COMMAND, spend_name_and_amount)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

SAVE = 1


async def save_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    await update.message.reply_text("Please enter how much you saved today,( e.g 500 1000)")


async def save_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    whole = update.message.text.strip()
    amounts = whole.split()

    if not all(i.isdigit for i in amounts):
        await update.message.reply_text("Please enter Valid numbers (e.g 2346, 9870, 10000000!)")
        return SAVE

    amount = [float(i) for i in amounts]
    tracker = get_user_tracker(update.effective_user.id)
    total_saved = tracker.save_today(*amount)
    await update.message.reply_text("✅Your savings has been added!")

async def cancelled(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CANCELLED")
    return ConversationHandler.END


conv_handler3 = ConversationHandler(
    entry_points=[CommandHandler("savings", save_command)],
    states={
        SAVE: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_amount)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

INVEST = 1


async def invest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    await update.message.reply_text("Enter name and amount of what you invested in this week")


async def invest_name_and_cost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().split()

    if not text[-1].replace(".", "", 1).isdigit():
        await update.message.reply_text("please enter valid format (e.g 'real estate 300000')")
        return INVEST

    cost = float(text[-1])
    name = "".join(text[:-1])
    tracker = get_user_tracker(update.effective_user.id)
    total_invested = (name, cost)

    await update.message.reply_text("Investment has successfully been saved to database!")

async def cancelled(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CANCELLED")
    return ConversationHandler.END


conv_handler4 = ConversationHandler(
    entry_points=[CommandHandler("investments", invest_command)],
    states={
        INVEST: [MessageHandler(filters.TEXT & ~filters.COMMAND, invest_name_and_cost)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

async def weekly_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)

    try:
        tracker.weekly_amounts()

        earn = getattr(tracker, "earn_total", 0)
        spent = getattr(tracker, "spend_total",0)
        leftover = earn - spent

        status_emoji = "📈" if leftover > 0 else "📉" if leftover < 0 else "➖"

        await update.message.reply_text(
f"""You earned {earn: ,.2f} this week, \n
you spent {spent: ,.2f} this week, \n
your leftover is {status_emoji}#{leftover: ,.2f}this week\n
{'🎉 Great job staying positive!' if leftover > 0 else '⚠️ You spent more than you earned this week.' if leftover < 0 else 'You broke even this week.'}""")

    except FileNotFoundError:
        await update.message.reply_text("📝 No data found yet. Start by adding some earnings or expenses!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating weekly summary: {str(e)}")


async def totals_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)

    try:
        tracker.tottal_earned()
        earned = getattr(tracker, "total_earned", 0)
        tracker.tottal_spent()
        spent = getattr(tracker, "total_spent", 0)
        tracker.starting_date()
        date = getattr(tracker, "beginning_date")
        tracker.tottal_saved()
        saved = getattr(tracker, "total_saved", 0)
        tracker.tottal_invested()
        invested = getattr(tracker, "total_invested", 0)

        await update.message.reply_text(f"""
📊TOTALS
You've;\n
💰earned: {earned}\n
💸spent: {spent}\n
🪙saved: {saved}\n
💵invested:{invested}\n
📅since {date}\n
""")
    except FileNotFoundError:
        await update.message.reply_text("📝 No data found yet. Start by adding some transactions!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating totals: {str(e)}")



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text  # whatever the user typed

    await update.message.reply_text(
        f"🤖 I didn't recognize \"{user_text}\".\n"
        "💡 Try one of these commands instead:\n"
        "/weekly – See your weekly summary\n"
        "/totals – See your totals\n"
        "/projections – Future projections\n"
        "/developer – Info about the developer\n"
        "/support – Tip your boy"
    )


def main():
    print("starting bot 🤖.....")

    application = Application.builder().token(TOKEN).build()
    application.add_handler(conv_handler)
    application.add_handler(conv_handler2)
    application.add_handler(conv_handler3)
    application.add_handler(conv_handler4)
    application.add_handler(conv_handler_date)
    application.add_handler(CommandHandler("start",start_command))
#    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("weekly", weekly_command))
    application.add_handler(CommandHandler("totals", totals_command))
#    application.add_handler(CommandHandler("projections", projections_command))
#    application.add_handler(CommandHandler("developer", developer_command))
#    application.add_handler(CommandHandler("support", support_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running! Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()


