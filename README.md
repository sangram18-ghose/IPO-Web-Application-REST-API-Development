# IPO Web Application REST API Development

Provides detailed IPO info including company details, pricing, dates, and performance metrics. Features user auth, admin dashboard, and downloadable PDFs.

## Tech Stack

- Python/Django
- Django REST Framework
- PostgreSQL
- HTML/CSS/JavaScript
- Bootstrap
- PowerShell
- Shell

## Features

- Detailed IPO information including company details, pricing, dates, and performance metrics.
- User authentication.
- Admin dashboard.
- Downloadable PDFs.

## Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- Git

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sangram18-ghose/IPO-Web-Application-REST-API-Development.git
   cd IPO-Web-Application-REST-API-Development
   ```

## Setting Up PostgreSQL Database

1. **Install PostgreSQL:**

   Make sure PostgreSQL is installed on your system. You can download it from the official [PostgreSQL website](https://www.postgresql.org/download/).

2. **Create a PostgreSQL Database and User:**

   Once PostgreSQL is installed, create a new database and a user for your Django application. You can do this using the PostgreSQL command-line interface (`psql`) or a graphical tool like pgAdmin.

   Open your terminal and run the following commands:



```sql
CREATE DATABASE bluestock;
CREATE USER daiyanalam WITH PASSWORD '12345';
ALTER ROLE daiyanalam SET client_encoding TO 'utf8';
ALTER ROLE daiyanalam SET default_transaction_isolation TO 'read committed';
ALTER ROLE daiyanalam SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bluestock TO daiyanalam;
```




3. **Install PostgreSQL Adapter for Python:**
```sh
pip install psycopg2-binary
```



4. **Configure Django Settings:**
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bluestock',
        'USER': 'daiyanalam',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```



5. **Apply Migrations:**
Run the following commands to apply migrations and start the server:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



5. **6. Video Guide**
 - [Video Link] (https://drive.google.com/file/d/1jUYqTqp_CTMRYu6FKNIT5327IPQh0fYk/view?usp=)
