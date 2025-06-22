from telegram.ext import Updater, CommandHandler
from django.conf import settings
from .models import TelegramUser

def start(update, context):
    username = update.message.from_user.username or "Unknown"
    TelegramUser.objects.get_or_create(username=username)
    update.message.reply_text(f"Hello {username}! You've been registered 🚀")

def run_bot():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
