# 🤖 Telegram Bot + Django REST API Project

This is a full-stack Django + Telegram Bot project I built as part of my internship assignment. It includes:

✅ JWT authentication  
✅ Public and protected API endpoints  
✅ Telegram Bot integration  
✅ Celery + Redis for background tasks  
✅ Clean GitHub repository with .gitignore and all best practices

---

## 🚀 Key Features

1. **Django REST Framework API**
   - Built with DRF and secured using JWT tokens
   - Public and protected routes (tested via Postman)

2. **Telegram Bot Functionality**
   - Greets new users with a custom message and stores their info
   - Sends:
     - Text replies
     - A PDF file (`example.pdf`)
     - An image (`image.jpg`)
     - A voice message (`voice.ogg`)

3. **Celery + Redis**
   - Asynchronous job handling (extensible for background tasks like logging, alerts, etc.)

4. **Clean Codebase**
   - Proper `.gitignore` to exclude virtual environments and cache
   - Virtualenv used for dependency isolation

---

## 🛠️ Technologies Used

- **Backend**: Django 5.2, Django REST Framework, djangorestframework-simplejwt  
- **Bot**: python-telegram-bot 13.15  
- **Async**: Celery + Redis  
- **Version Control**: Git & GitHub  
- **Tested On**: Python 3.11 (recommended)

---

## 🧪 How to Run This Project

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # For Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Django server
python manage.py runserver

# 4. Run Telegram Bot
python run_telegram_bot.py



## 📁 Folder Structure

Telegram_bot/
├── core/                   # Django app for APIs
├── telegram_bot/           # Bot logic and models
├── internship_project/     # Django project config
├── run_telegram_bot.py     # Script to start bot
├── requirements.txt
├── .gitignore
└── README.md
