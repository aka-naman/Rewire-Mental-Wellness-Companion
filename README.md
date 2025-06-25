# Rewire: Mental Wellness Tracker

A modern, secure, and visually stunning Django web application for tracking mental wellness, journaling, and mood. Inspired by the [Django-Authentication-Admin-Access-Project](https://github.com/msoni6620/Django-Authentication-Admin-Access-Project), this project features a cosmic dark theme, user authentication, journaling, mood tracking, and a beautiful galaxy background powered by Three.js.

---

## Features

- **User Registration & Authentication**
- **Profile Management**
- **Journal Entries** (Create, Read, Update, Delete)
- **Mood Tracker** (Daily mood logging)
- **Dashboard** with activity stats and streaks
- **Cosmic Dark Theme** (Glassmorphism, indigo, pastel, soft glows)
- **Three.js Galaxy Background** on all pages
- **Responsive Design**
- **Admin Panel** for user and content management
- **Secure static/media file handling**

---

## Demo

Deployed on PythonAnywhere: [https://akanaman.pythonanywhere.com](https://akanaman.pythonanywhere.com)

---

## Screenshots


![Screenshot 2025-06-25 221355](https://github.com/user-attachments/assets/e0fe0ef2-9b63-4867-935d-868c9146cfbb)

---

## Tech Stack

- **Backend:** Django 5.2
- **Frontend:** HTML5, CSS3, JavaScript (Three.js for galaxy effect)
- **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)
- **Deployment:** PythonAnywhere

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rewire.git
cd rewire
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# Or: source venv/bin/activate  # On Mac/Linux
pip install -r requirements.txt
```

### 3. Configure Environment Variables

- Create a `.env` file in the project root:

```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=akanaman.pythonanywhere.com,localhost,127.0.0.1
```

- **Never commit your `.env` or secret keys to GitHub!**

### 4. Apply Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Collect Static Files

```bash
python manage.py collectstatic
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000)

---

## Deployment (PythonAnywhere)

1. Upload your project files to PythonAnywhere.
2. Set up a virtual environment and install dependencies.
3. Set environment variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS) in the PythonAnywhere dashboard.
4. Run migrations and collectstatic.
5. Configure static and media file mappings:
   - `/static/` → `/home/yourusername/rewire/staticfiles/`
   - `/media/` → `/home/yourusername/rewire/media/`
6. Reload your web app.

See the [PythonAnywhere deployment guide](https://help.pythonanywhere.com/pages/DeployingDjango/) for details.

---

## Folder Structure

```
rewire/
├── core/
│   ├── static/
│   ├── templates/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
├── rewire/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── media/
├── staticfiles/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Security & Best Practices

- Use environment variables for all secrets and sensitive settings.
- Add `.env` and `db.sqlite3` to `.gitignore`.
- Set `DEBUG = False` in production.
- Use strong, unique passwords for admin and users.
- Regularly update dependencies.

---

## Credits

- [Django-Authentication-Admin-Access-Project](https://github.com/msoni6620/Django-Authentication-Admin-Access-Project) for project inspiration.
- [Three.js Galaxy Background](https://github.com/mrdoob/three.js/) for the cosmic effect.

---

## License

This project is licensed under the MIT License.
