📝 Django Blog A simple and clean blog built with Django. The project includes an admin panel, post categories, and a responsive UI using custom HTML and CSS. The blog is fully in English and ready for deployment or local testing.

🚀 Features 🗂 Create, edit, and delete blog posts

📚 Organize posts by categories

🧭 Posts ordered by publication date

🔐 Django Admin Panel for full control

💻 Responsive layout using custom styles

💾 Requirements Python 3.8+

pip (Python package installer)

Git (optional, for cloning)

Virtual environment recommended

📦 Installation Guide

Clone the repository bash Copy Edit git clone https://github.com/fxcker01/blog.git cd blog
Create a virtual environment (optional but recommended) bash Copy Edit python -m venv venv source venv/bin/activate # On Linux/macOS venv\Scripts\activate # On Windows
Install dependencies bash Copy Edit pip install -r requirements.txt
Apply database migrations bash Copy Edit python manage.py migrate
Create your own admin user bash Copy Edit python manage.py createsuperuser This will ask for:
Username

Email (can be fake)

Password

You’ll use these credentials to log in at /admin/.

Run the development server bash Copy Edit python manage.py runserver Open your browser:
Blog: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

🔐 Admin Panel Access Only you will have access to your own admin panel. The admin user is created locally on your machine when you run createsuperuser. Do not share your credentials — every user should create their own admin.

🌍 Deployment (Render or other) To deploy on Render, make sure you have:

requirements.txt

Procfile

ALLOWED_HOSTS set properly in settings.py

Secret key and debug settings configured for production

(Deployment instructions can be added later)

🙌 Auth
