import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')
django.setup()

from telegram_bot.bot import run_bot

run_bot()
