from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import logging
from telegram import Update
import os

# Read token properly
with open(".env", "r") as file:
    TOKEN = file.read().strip()

BOT_USERNAME = "@miniFinanceTrackingBot"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.info("Starting Bot")

user_trackers = {}

# Import your model - assuming it exists and works
try:
    from miniPerformanceModel import BudgetModel, WeeksPassed, Calc
except ImportError:
    logging.error("Could not import miniPerformanceModel. Please ensure the file exists and is properly implemented.")
    exit(1)


def get_user_tracker(user_id):
    if user_id not in user_trackers:
        user_trackers[user_id] = Calc()  # Initialize as instance, not class
    return user_trackers[user_id]


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🏦 Welcome to your Friendly Finance tracking bot 🦇

📅 SET START DATE 
• /startdate - Set your budgeting start date

💰 ADD TODAY'S EARNINGS 
• /earnings - Add your daily earnings

💸 ADD TODAY'S EXPENSES
• /expenses - Add expenses with name and cost

🪙 ADD TODAY'S SAVINGS 
• /savings - Add your daily savings

💴 ADD TODAY'S INVESTMENTS 🧧
• /investments - Add investment details

📊 VIEW REPORTS  
• /weekly - This week's summary
• /totals - All-time totals
• /projection - Project n week(s) ahead

Let's grow and monitor your finances together! 🚀 
""")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📊 Reports
• `/weekly` - This week's earnings vs spending
• `/totals` - All-time totals
• `/projection` - Forecast n weeks ahead

⚙️ Setup
• `/startdate` - Set when you started budgeting

💡 Tips
- Use quotes for multi-word items: "Phone bill" 100
- All amounts are in Naira (₦)

👨‍💻 Developer
• /developer - About the developer
• /support - Support the developer
""")


# Date setting conversation
DATE = 1


async def start_date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💡 Usage: Enter date as 2025 8 28 (year month day)")
    return DATE


async def start_date_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        date = update.message.text.strip()
        parts = date.split()

        if len(parts) != 3:
            await update.message.reply_text("💡 Please enter exactly 3 numbers: year month day (e.g., 2025 8 28)")
            return DATE

        if not all(p.isdigit() for p in parts):
            await update.message.reply_text("💡 Please enter valid numbers for year month day")
            return DATE

        year, month, day = map(int, parts)

        # Basic date validation
        if year < 2000 or year > 2030 or month < 1 or month > 12 or day < 1 or day > 31:
            await update.message.reply_text("💡 Please enter a valid date")
            return DATE

        tracker = get_user_tracker(update.effective_user.id)
        tracker.starting_date(year, month, day)

        await update.message.reply_text(f"""✅ Start Date Set!

📅 Started budgeting: {year}-{month:02d}-{day:02d}
⏰ You've been budgeting for {getattr(tracker, 'how_long_weeks', 0)} week(s)""")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error setting date: {str(e)}")
        return ConversationHandler.END


# Earnings conversation
AMOUNT = 1


async def earn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter earning amounts (e.g., 500 1000 2000)")
    return AMOUNT


async def earn_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = update.message.text.strip()
        parts = amount.split()

        if not parts:
            await update.message.reply_text("Please enter at least one amount")
            return AMOUNT

        # Check if all parts are valid numbers
        amounts = []
        for p in parts:
            try:
                amounts.append(float(p))
            except ValueError:
                await update.message.reply_text("Please enter valid numbers only")
                return AMOUNT

        if any(amt < 0 for amt in amounts):
            await update.message.reply_text("Please enter positive amounts only")
            return AMOUNT

        tracker = get_user_tracker(update.effective_user.id)
        total_earned = tracker.earn_daily(*amounts)

        await update.message.reply_text(f"""✅ Added ₦{sum(amounts):,.2f}!
💰 Total earned today: ₦{total_earned:,.2f}""")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error adding earnings: {str(e)}")
        return ConversationHandler.END


# Expenses conversation
SPEND = 1


async def spent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter expense name and amount (e.g., 'food 500' or 'transport 200')")
    return SPEND


async def spend_name_and_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip()
        parts = text.split()

        if len(parts) < 2:
            await update.message.reply_text("Please enter both name and amount (e.g., 'food 500')")
            return SPEND

        # Try to extract cost from last part
        try:
            cost = float(parts[-1])
        except ValueError:
            await update.message.reply_text("Please enter a valid amount as the last part")
            return SPEND

        if cost < 0:
            await update.message.reply_text("Please enter a positive amount")
            return SPEND

        name = " ".join(parts[:-1])
        if not name:
            await update.message.reply_text("Please enter a name for the expense")
            return SPEND

        tracker = get_user_tracker(update.effective_user.id)
        total_spent = tracker.spent_today(name, cost)

        await update.message.reply_text(f"✅ Added expense: {name} - ₦{cost:,.2f}")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error adding expense: {str(e)}")
        return ConversationHandler.END


# Savings conversation
SAVE = 1


async def save_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter how much you saved today (e.g., 500 1000)")
    return SAVE


async def save_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        whole = update.message.text.strip()
        parts = whole.split()

        if not parts:
            await update.message.reply_text("Please enter at least one amount")
            return SAVE

        amounts = []
        for part in parts:
            try:
                amounts.append(float(part))
            except ValueError:
                await update.message.reply_text("Please enter valid numbers only")
                return SAVE

        if any(amt < 0 for amt in amounts):
            await update.message.reply_text("Please enter positive amounts only")
            return SAVE

        tracker = get_user_tracker(update.effective_user.id)
        total_saved = tracker.save_today(*amounts)

        await update.message.reply_text(f"✅ Savings added: ₦{sum(amounts):,.2f}")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error adding savings: {str(e)}")
        return ConversationHandler.END


# Investment conversation
INVEST = 1


async def invest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter investment name and amount (e.g., 'real estate 300000')")
    return INVEST


async def invest_name_and_cost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip()
        parts = text.split()

        if len(parts) < 2:
            await update.message.reply_text("Please enter both investment name and amount")
            return INVEST

        try:
            cost = float(parts[-1])
        except ValueError:
            await update.message.reply_text("Please enter a valid amount as the last part")
            return INVEST

        if cost < 0:
            await update.message.reply_text("Please enter a positive amount")
            return INVEST

        name = " ".join(parts[:-1])
        if not name:
            await update.message.reply_text("Please enter a name for the investment")
            return INVEST

        tracker = get_user_tracker(update.effective_user.id)
        # Assuming there's an invest_today method
        tracker.invest_today(name, cost)

        await update.message.reply_text(f"✅ Investment added: {name} - ₦{cost:,.2f}")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error adding investment: {str(e)}")
        return ConversationHandler.END


# Cancel handler
async def cancelled(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Operation cancelled")
    return ConversationHandler.END


# Create conversation handlers
conv_handler_date = ConversationHandler(
    entry_points=[CommandHandler("startdate", start_date_command)],
    states={
        DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, start_date_date)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

conv_handler_earnings = ConversationHandler(
    entry_points=[CommandHandler("earnings", earn_command)],
    states={
        AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, earn_amount)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

conv_handler_expenses = ConversationHandler(
    entry_points=[CommandHandler("expenses", spent_command)],
    states={
        SPEND: [MessageHandler(filters.TEXT & ~filters.COMMAND, spend_name_and_amount)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

conv_handler_savings = ConversationHandler(
    entry_points=[CommandHandler("savings", save_command)],
    states={
        SAVE: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_amount)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

conv_handler_investments = ConversationHandler(
    entry_points=[CommandHandler("investments", invest_command)],
    states={
        INVEST: [MessageHandler(filters.TEXT & ~filters.COMMAND, invest_name_and_cost)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)

# Projections conversation
PROJECTIONS = 1


async def projections_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter number of weeks to project for (e.g., 4)")
    return PROJECTIONS


async def projections_duration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        number = update.message.text.strip()

        if not number.isdigit():
            await update.message.reply_text("Please enter a valid positive integer!")
            return PROJECTIONS

        weeks = int(number)
        if weeks <= 0:
            await update.message.reply_text("Please enter a positive number of weeks!")
            return PROJECTIONS

        tracker = get_user_tracker(update.effective_user.id)

        # Ensure totals are calculated first
        tracker.tottal_earned()
        tracker.tottal_spent()
        tracker.tottal_saved()
        tracker.tottal_invested()

        tracker.projections(weeks)

        spending = getattr(tracker, "projected_spending", 0)
        earning = getattr(tracker, "projected_earning", 0)
        savings = getattr(tracker, "projected_savings", 0)

        await update.message.reply_text(f"""📊 {weeks} Week Projection:
💰 Projected earnings: ₦{earning:,.2f}
💸 Projected spending: ₦{spending:,.2f}
🪙 Projected savings: ₦{savings:,.2f}
📈 Net change: ₦{earning - spending:,.2f}""")

        return ConversationHandler.END
    except ZeroDivisionError:
        await update.message.reply_text("❌ Cannot project - you haven't been budgeting long enough yet!")
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating projections: {str(e)}")
        return ConversationHandler.END


conv_handler_projections = ConversationHandler(
    entry_points=[CommandHandler("projection", projections_command)],
    states={
        PROJECTIONS: [MessageHandler(filters.TEXT & ~filters.COMMAND, projections_duration)],
    },
    fallbacks=[CommandHandler("cancel", cancelled)]
)


# Report commands
async def weekly_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        tracker = get_user_tracker(user_id)

        tracker.weekly_amounts()

        earn = getattr(tracker, "earn_total", 0)
        spent = getattr(tracker, "spend_total", 0)
        leftover = earn - spent

        status_emoji = "📈" if leftover > 0 else "📉" if leftover < 0 else "➖"

        status_msg = ("🎉 Great job staying positive!" if leftover > 0 else
                      "⚠️ You spent more than you earned this week." if leftover < 0 else
                      "You broke even this week.")

        await update.message.reply_text(f"""📊 Weekly Summary:
💰 Earned: ₦{earn:,.2f}
💸 Spent: ₦{spent:,.2f}
{status_emoji} Net: ₦{leftover:,.2f}

{status_msg}""")

    except FileNotFoundError:
        await update.message.reply_text("📝 No data found yet. Start by adding some earnings or expenses!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating weekly summary: {str(e)}")


async def totals_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        tracker = get_user_tracker(user_id)

        tracker.tottal_earned()
        earned = getattr(tracker, "total_earned", 0)
        tracker.tottal_spent()
        spent = getattr(tracker, "total_spent", 0)
        tracker.tottal_saved()
        saved = getattr(tracker, "total_saved", 0)
        tracker.tottal_invested()
        invested = getattr(tracker, "total_invested", 0)

        # Get start date
        date = getattr(tracker, "beginning_date", "Not set")

        await update.message.reply_text(f"""📊 ALL-TIME TOTALS

💰 Total earned: ₦{earned:,.2f}
💸 Total spent: ₦{spent:,.2f}
🪙 Total saved: ₦{saved:,.2f}
💵 Total invested: ₦{invested:,.2f}

📅 Since: {date}
📈 Net worth change: ₦{earned - spent:,.2f}""")

    except FileNotFoundError:
        await update.message.reply_text("📝 No data found yet. Start by adding some transactions!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating totals: {str(e)}")


async def developer_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""👨‍💻 This bot was created by an Akatsuki member

📧 Contact: batmansofficialmail@gmail.com
☁️ GitHub: imbatmanfrl
💭 Telegram: @imbatmanfrfrl""")


async def support_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""💝 Support the Developer

Here are my crypto wallet addresses if you're feeling generous:

🪙 USDT: [Your USDT address]
💎 SOLANA: [Your Solana address]
💠 ETHEREUM: [Your ETH address]

You can also DM the developer for fiat transfer options.
Thanks for supporting the project! 🚀""")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(f"""🤖 I didn't recognize "{user_text}".

💡 Try one of these commands instead:
• /weekly – See your weekly summary
• /totals – See your totals  
• /projection – Future projections
• /help – Full command list
• /developer – Info about the developer
• /support – Support the project""")


def main():
    print("Starting bot 🤖...")

    application = Application.builder().token(TOKEN).build()

    # Add conversation handlers
    application.add_handler(conv_handler_date)
    application.add_handler(conv_handler_earnings)
    application.add_handler(conv_handler_expenses)
    application.add_handler(conv_handler_savings)
    application.add_handler(conv_handler_investments)
    application.add_handler(conv_handler_projections)

    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("weekly", weekly_command))
    application.add_handler(CommandHandler("totals", totals_command))
    application.add_handler(CommandHandler("developer", developer_command))
    application.add_handler(CommandHandler("support", support_command))

    # Handle unrecognized messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running! Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()