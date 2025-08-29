from telegram.ext import  Application,CommandHandler,MessageHandler,filters,ContextTypes
import logging
from telegram import Update
import re
import json
import asyncio
import os

with open (".env","r")as file:
    TOKEN = file.read()

BOT_USERNAME = "@miniFinanceTrackingBot"

logging.basicConfig(format="%(acstime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.info("Strating Bot")

def start_command(update,context):
    update.message.reply_text("Hello there welcome to A Financial tracker bot")