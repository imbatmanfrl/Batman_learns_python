"""from typing import final
from telegram import  Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
telegram = "7989685901:AAHtMSa4VEBImTH1mVrMYGCSQzI27lgkVZ0"

BOT_USERNAME: final = "@MiniAmaterasuBudgetModelbot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Welcome To Mini Amaterasu 0.5!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a BUDGETING assistant, you wallet tracker ")


async def batman_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Batman")

def handle_responses(text: str) -> str:
    processed = str(text.lower())
    if "hello" in processed:
        return "hey there"

    if "batman" in processed:
        return "🦇"

    return "Here we go"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = str(update.message.chat.type)
    text = str(update.message.text)

    print(f'user({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text = str(text.replace(BOT_USERNAME,'')).strip()
            response = str(handle_responses(new_text))
        else:
            return
    else:
        response = str (handle_responses(text))

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update {update} caused error {context.error}")

if __name__ == "__main__":
    print("Starting Bot...")
    app  = Application.builder().token(telegram).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("batman", batman_command))

    print("polling....")
    app.run_polling(poll_interval=3)
#   app.add_handler(MessageHandler(filters.TEXT handle_message))

"""