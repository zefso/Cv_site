# 👨‍💻 Roman Horbach — Professional Portfolio Website

![Django](https://img.shields.io/badge/Framework-Django%205.2-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Language-Python%203.11-blue?style=for-the-badge&logo=python)
![i18n](https://img.shields.io/badge/Localization-i18n%20Support-orange?style=for-the-badge)

Modern, high-performance, **multilingual** portfolio website showcasing my journey from **Arduino electronics** → **Machine Learning** → **Backend Development**.

## 🌍 Key Features

- **Multilingual support** (English / Ukrainian / Polish) using **Django native i18n**
- Dynamic language prefixes in URLs (`/en/`, `/pl/`, `/uk/`)
- Session + cookie based language preference
- High-quality manual translations (PO/MO files)
- Responsive design with **Bootstrap 5**
- Smooth scroll animations via **AOS**
- Custom interactive timeline component
- Telegram Bot integration for contact form (async)
- Secure credentials handling via `.env`

## 🛠️ Tech Stack

| Category          | Technology                          |
|-------------------|-------------------------------------|
| Backend           | Django 5.2, Python 3.11             |
| Frontend          | Bootstrap 5, HTML5, CSS3            |
| Animations        | AOS (Animate on Scroll)             |
| Internationalization | Django i18n + gettext            |
| Contact form      | Telegram Bot API (python-telegram-bot) |
| Environment       | python-dotenv                       |
| Deployment-ready  | gunicorn + whitenoise (recommended) |

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/zefso/Cv_site
cd resume_site
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create .env file in the root folder
```bash
#    Example content:
#    SECRET_KEY=your-very-long-random-secret-key
#    DEBUG=True
#    TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
#    TELEGRAM_CHAT_ID=123456789
```

### 4. Apply migrations & compile translations
```bash
python manage.py migrate
python manage.py compilemessages
```
### 5. Run development server
```bash
python manage.py runserver
Open → http://127.0.0.1:8000/
```
### 📂 Project Structure (main parts)
```bash
resume_site/          
├── .env              
├── .gitignore         
├── manage.py          
├── requirements.txt
├── README.md
├── main/              
│   ├── views.py
│   └── ...
└── resume_site/       
    ├── settings.py
    └── ...               
```
## 🎓 Education
- Double Degree Program — Software Engineering

- KROK University (Kyiv, Ukraine)
- DSW University of Lower Silesia (Wrocław, Poland)

## 📬 Contact & Links

- Telegram → @zefsooo
- GitHub   → zefso
- LinkedIn → Roma Horbach


### © 2026 Roman Horbach. Built with ❤️ and Python.