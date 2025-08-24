from typing import final
from telegram import  Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, ConversationHandler
from miniPerformanceModel import BudgetModel,WeeksPassed,Spending,Calc

TOKEN = "7989685901:AAHtMSa4VEBImTH1mVrMYGCSQzI27lgkVZ0"

BOT_USERNAME = "@MiniAmaterasuBudgetModelbot"

EARNINGS,EXPENDITURE,SAVINGS,INVESTMENTS = range(4)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello, Welcome to Mini Amaterasu 0.5 🦇!. "
                                    f"What is Your weekly Earning?")
    return EARNINGS

async def earnings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["earnings"]=int(update.message.text)
    await update.message.reply_text(f"How much did you spend this week?")
    return EXPENDITURE

async def expenditures(update: Update,context: ContextTypes.DEFAULT_TYPE):
    context.user_data["expenses"] =int(update.message.text)
    #update.message.text → gets what the user typed (e.g. "15000") input isnt used in receiving input for bots
    #context.user_data["earnings"] = ... → saves it to that user's session.
    await update.message.reply_text(f"How muc did you save this week")
    return SAVINGS

async def savings(update:Update,context: ContextTypes.DEFAULT_TYPE):
    context.user_data["savings"] = int(update.message.text)
    await update.message.reply_text(f"How much did you invest this week??")
    return INVESTMENTS

async def investments(update:Update,context: ContextTypes.DEFAULT_TYPE):
    context.user_data["investments"] = int(update.message.text)

    model = BudgetModel(
        context.user_data["earnings"],
        context.user_data["expenses"],
        context.user_data["savings"],
        context.user_data["investments"]
    )

    await update.message.reply_text(f"Inputs received ({model.weekly_earnings},{model.weekly_savings}{model.weekly_expenditure},{model.weekly_investments})")
    return ConversationHandler.END


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start_command))
app.add_handler(CommandHandler("earnings",earnings))
app.add_handler(CommandHandler("expenditures",expenditures))
app.add_handler(CommandHandler("savings",savings))
app.add_handler(CommandHandler("investments",investments))
print("bot is running")
app.run_polling()


