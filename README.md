# django-flexblog

A minimal, customizable Django-based blog engine with authentication, author profiles, article creation, pagination, and Bootstrap-adaptive layout. Ideal for personal use, quick startup projects, or client-ready blog solutions.

🛠 Technologies Used
Backend:
Python, Django

Frontend:
Bootstrap, HTML, CSS

Database:
SQLite 

Deployment:
Railway, Git, GitHub

🚀 Features
User authentication (Sign Up, Sign In, Log Out)

Profile management with avatar upload

CRUD functionality for blog posts

Responsive and mobile-friendly design

Clean, modular codebase for future improvements and scalability

---

## ⚙️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/fxcker01/django-flexblog.git
cd django-flexblog
```

### 2. Set up virtualenv (recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations and create superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the dev server
```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/` 🎉

---

## 🌐 Deploy to Railway
Add this to your `Procfile`:
```procfile
web: python manage.py collectstatic --noinput && gunicorn djangoBlog.wsgi:application --bind 0.0.0.0:$PORT
```

Ensure `DEBUG = False`, and environment variables are set on Railway for secret key, allowed hosts, etc.

---

## 📂 Project Structure
```
djangoBlog/
├── blog/              # Blog logic and templates/blog/
│   └── templates/blog/
├── users/             # User auth/profile handling
│   └── templates/users/
├── blog/static/blog/  # Custom CSS
├── media/             # Uploaded avatars
├── requirements.txt
├── Procfile
├── LICENSE
└── README.md
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Created by [fxcker01](https://github.com/fxcker01) 🖤
