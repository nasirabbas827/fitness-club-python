# fitness_club_python_final  

A compact Django‑based web application that models a fitness club’s core operations – customers, instructors, workouts, and reporting. The project showcases a clean separation of concerns (models, forms, admin, views, URLs) and includes a full migration history for easy database setup.

---

## Overview  

`fitness_club_python_final` implements a simple yet functional fitness‑club management system. It allows staff to:

* Register customers and instructors.  
* Define workouts and assign instructors.  
* Track daily fitness reports and customer fee reports.  
* Generate basic analytics via the Django admin interface.

The codebase is intentionally lightweight, making it ideal for learning Django fundamentals, extending with new features, or using as a starter template for similar domain‑specific apps.

---

## Features  

| Feature | Description |
|---------|-------------|
| **Customer Management** | Store personal details, membership status, and fee history. |
| **Instructor Management** | Track instructor salaries, assigned workouts, and availability. |
| **Workout Scheduling** | Define workouts, link them to instructors, and record dates. |
| **Reporting** | Daily fitness reports and customer fee reports generated via Django admin. |
| **Data Migration History** | 14 sequential migrations covering schema evolution and cleanup. |
| **Backup Data** | `backup.json` provides a sample fixture for quick data import. |

---

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **Framework** | Django 4.x (Python 3.9+) |
| **Database** | SQLite (default) – can be swapped for PostgreSQL, MySQL, etc. |
| **Language** | Python |
| **Front‑end** | Django templating (HTML/CSS – minimal, extendable) |
| **Version Control** | Git |

---

## Installation  

1. **Clone the repository**  

   ```bash
   git clone https://github.com/your-username/fitness_club_python_final.git
   cd fitness_club_python_final
   ```

2. **Create and activate a virtual environment**  

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  

   If a `requirements.txt` is present:

   ```bash
   pip install -r requirements.txt
   ```

   Otherwise install Django directly:

   ```bash
   pip install Django==4.*
   ```

4. **Apply migrations**  

   ```bash
   python manage.py migrate
   ```

5. **(Optional) Load sample data**  

   ```bash
   python manage.py loaddata backup.json
   ```

6. **Create a superuser for the admin interface**  

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**  

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser. The admin panel is available at `http://127.0.0.1:8000/admin/`.

---

## Usage  

| Action | Command / Steps |
|--------|-----------------|
| **Start the app** | `python manage.py runserver` |
| **Access admin** | Log in with the superuser credentials at `/admin/`. |
| **Add data** | Use the admin UI to create customers, instructors, workouts, etc. |
| **Run tests** *(if