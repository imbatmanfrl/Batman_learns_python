import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re
from datetime import datetime
import json
import os

# Your existing classes
from miniPerformanceModel import BudgetModel, WeeksPassed, Calc

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot configuration
TOKEN = "7989685901:AAHtMSa4VEBImTH1mVrMYGCSQzI27lgkVZ0"
BOT_USERNAME = "@MiniAmaterasuBudgetModelbot"

# Create a global instance for each user (in production, you'd use a database)
user_trackers = {}

def get_user_tracker(user_id):
    """Get or create a Calc instance for a user"""
    if user_id not in user_trackers:
        user_trackers[user_id] = Calc()
    return user_trackers[user_id]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    welcome_message = """
🏦 Welcome to Budget Tracker Bot! 💰

Track your finances easily:

💵 **Add Earnings:**
• /earn 2500
• /earn 1000 500 (multiple sources)

💸 **Add Expenses:**
• /spend Coffee 50
• /spend "Transport" 200

💾 **Add Savings:**
• /save 1000

📈 **Add Investments:**
• /invest "Stocks" 5000

📊 **View Reports:**
• /weekly - This week's summary
• /totals - All-time totals
• /projection 4 - Project 4 weeks ahead

🗓️ **Set Start Date:**
• /startdate 2025 8 28

Let's start tracking your money! 🚀
"""
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message."""
    help_text = """
📋 **Available Commands:**

💰 **Money In:**
• `/earn 2500` - Add daily earnings
• `/save 1000` - Add savings

💸 **Money Out:**
• `/spend Coffee 50` - Add expense
• `/invest Stocks 5000` - Add investment

📊 **Reports:**
• `/weekly` - This week's earnings vs spending
• `/totals` - All-time totals
• `/projection 4` - Forecast 4 weeks ahead

⚙️ **Setup:**
• `/startdate 2025 8 28` - Set when you started budgeting

💡 **Tips:**
- Use quotes for multi-word items: `/spend "Phone bill" 100`
- All amounts are in Naira (₦)
"""
    await update.message.reply_text(help_text)

async def earn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /earn command"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    if not context.args:
        await update.message.reply_text("💡 Usage: /earn 2500 or /earn 1000 500 200")
        return
    
    try:
        amounts = [float(arg) for arg in context.args]
        total_earned = tracker.earn_daily(*amounts)
        
        await update.message.reply_text(
            f"✅ **Earnings Added!**\n"
            f"💰 Amount: ₦{total_earned:,.2f}\n"
            f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
            f"Use /weekly to see this week's summary!"
        )
    except ValueError:
        await update.message.reply_text("❌ Please use valid numbers only.\nExample: /earn 2500")

async def spend_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /spend command"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    if len(context.args) < 2:
        await update.message.reply_text("💡 Usage: /spend Coffee 50 or /spend \"Phone bill\" 100")
        return
    
    try:
        # Join all args except the last one as item name, last arg as amount
        item = " ".join(context.args[:-1]).strip('"')
        amount = float(context.args[-1])
        
        tracker.spent_today(item, amount)
        
        await update.message.reply_text(
            f"✅ **Expense Added!**\n"
            f"🛍️ Item: {item}\n"
            f"💸 Amount: ₦{amount:,.2f}\n"
            f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
            f"Use /weekly to see this week's summary!"
        )
    except ValueError:
        await update.message.reply_text("❌ Invalid amount. Use: /spend Coffee 50")

async def save_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /save command"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    if not context.args:
        await update.message.reply_text("💡 Usage: /save 1000")
        return
    
    try:
        amounts = [float(arg) for arg in context.args]
        tracker.save_today(*amounts)
        total_saved = sum(amounts)
        
        await update.message.reply_text(
            f"✅ **Savings Added!**\n"
            f"💾 Amount: ₦{total_saved:,.2f}\n"
            f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}"
        )
    except ValueError:
        await update.message.reply_text("❌ Please use valid numbers only.\nExample: /save 1000")

async def invest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /invest command"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    if len(context.args) < 2:
        await update.message.reply_text("💡 Usage: /invest Stocks 5000")
        return
    
    try:
        name = " ".join(context.args[:-1]).strip('"')
        amount = float(context.args[-1])
        
        tracker.invest(name, amount)
        
        await update.message.reply_text(
            f"✅ **Investment Added!**\n"
            f"📈 Investment: {name}\n"
            f"💰 Amount: ₦{amount:,.2f}\n"
            f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}"
        )
    except ValueError:
        await update.message.reply_text("❌ Invalid amount. Use: /invest Stocks 5000")

async def weekly_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show weekly summary"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    try:
        tracker.weekly_amounts()
        
        earned = getattr(tracker, 'earn_total', 0)
        spent = getattr(tracker, 'spend_total', 0)
        leftover = earned - spent
        
        status_emoji = "📈" if leftover > 0 else "📉" if leftover < 0 else "➖"
        
        message = f"""
📊 **This Week's Summary:**

💰 **Earned:** ₦{earned:,.2f}
💸 **Spent:** ₦{spent:,.2f}
{status_emoji} **Balance:** ₦{leftover:,.2f}

{'🎉 Great job staying positive!' if leftover > 0 else '⚠️ You spent more than you earned this week.' if leftover < 0 else 'You broke even this week.'}
"""
        await update.message.reply_text(message)
        
    except FileNotFoundError:
        await update.message.reply_text("📝 No data found yet. Start by adding some earnings or expenses!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating weekly summary: {str(e)}")

async def totals_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show all-time totals"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    try:
        # Calculate totals
        earned_msg = tracker.tottal_earned()
        spent_msg = tracker.tottal_spent()
        saved_msg = tracker.tottal_saved()
        invested_msg = tracker.tottal_invested()
        
        message = f"""
📈 **All-Time Totals:**

💰 {earned_msg}
💸 {spent_msg}
💾 {saved_msg}
📊 {invested_msg}

📅 Since you started tracking your finances!
"""
        await update.message.reply_text(message)
        
    except FileNotFoundError:
        await update.message.reply_text("📝 No data found yet. Start by adding some transactions!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating totals: {str(e)}")

async def startdate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set starting date for budgeting"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    if len(context.args) != 3:
        await update.message.reply_text("💡 Usage: /startdate 2025 8 28 (year month day)")
        return
    
    try:
        year, month, day = map(int, context.args)
        tracker.starting_date(year, month, day)
        
        await update.message.reply_text(
            f"✅ **Start Date Set!**\n"
            f"📅 Started budgeting: {year}-{month:02d}-{day:02d}\n"
            f"⏰ You've been budgeting for {getattr(tracker, 'how_long_weeks', 0)} week(s)"
        )
    except ValueError:
        await update.message.reply_text("❌ Invalid date format. Use: /startdate 2025 8 28")
    except Exception as e:
        await update.message.reply_text(f"❌ Error setting start date: {str(e)}")

async def projection_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show financial projections"""
    user_id = update.effective_user.id
    tracker = get_user_tracker(user_id)
    
    if not context.args:
        await update.message.reply_text("💡 Usage: /projection 4 (number of weeks)")
        return
    
    try:
        weeks = int(context.args[0])
        
        # Make sure totals are calculated
        tracker.tottal_earned()
        tracker.tottal_spent()
        tracker.tottal_saved()
        
        tracker.projections(weeks)
        
        await update.message.reply_text(
            f"🔮 **{weeks}-Week Projection:**\n\n"
            f"Based on your current performance, here's what to expect!\n"
            f"Check the console output for detailed projections."
        )
    except ValueError:
        await update.message.reply_text("❌ Please provide a valid number of weeks.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error calculating projection: {str(e)}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular messages"""
    text = update.message.text.strip()
    
    # Try to parse quick expense format: "Coffee 50"
    pattern = r'^(.+?)\s+(\d+\.?\d*)$'
    match = re.match(pattern, text)
    
    if match:
        user_id = update.effective_user.id
        tracker = get_user_tracker(user_id)
        
        try:
            item = match.group(1).strip()
            amount = float(match.group(2))
            
            tracker.spent_today(item, amount)
            
            await update.message.reply_text(
                f"✅ **Quick Expense Added!**\n"
                f"🛍️ {item}: ₦{amount:,.2f}\n\n"
                f"💡 Use /weekly for weekly summary or /help for all commands!"
            )
        except ValueError:
            await update.message.reply_text(
                "💡 Try:\n"
                "• Coffee 50\n"
                "• /spend \"Phone bill\" 100\n"
                "• /help for all commands"
            )
    else:
        await update.message.reply_text(
            "💡 **Quick Commands:**\n"
            "• Coffee 50 (quick expense)\n"
            "• /earn 2500\n"
            "• /spend Coffee 50\n"
            "• /weekly (summary)\n"
            "• /help (all commands)"
        )

def main():
    """Start the bot."""
    print("🤖 Budget Bot is starting...")
    
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("earn", earn_command))
    application.add_handler(CommandHandler("spend", spend_command))
    application.add_handler(CommandHandler("save", save_command))
    application.add_handler(CommandHandler("invest", invest_command))
    application.add_handler(CommandHandler("weekly", weekly_command))
    application.add_handler(CommandHandler("totals", totals_command))
    application.add_handler(CommandHandler("startdate", startdate_command))
    application.add_handler(CommandHandler("projection", projection_command))
    
    # Add message handler for quick expenses
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    print("✅ Bot is running! Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()