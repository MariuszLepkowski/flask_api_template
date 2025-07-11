# Template for Flask REST API projects

This is a recruitment REST API task template built with Flask by Mariusz Łepkowski.  
It supports both local setup via virtual environment and Docker, and includes an integrated PostgreSQL database setup.

- Flask + RESTful architecture
- PostgreSQL integration via SQLAlchemy
- Input/output via JSON
- Ready for unit testing
- Minimal structure, easy to extend
- .env support for configuration
---

## Requirements

- Python 3.10+
- (Optional) Docker


## Setup 
```bash
# Clone the repo
git clone https://github.com/MariuszLepkowski/flask_api_template
mv flask_api_template <your-project-name>
cd <your-project-name>
```

Tip:
Changing the folder name (e.g. to music-api-task, books-crud, etc.) will help clearly separate different types of tasks.
It also affects the default names of Docker containers when using docker-compose.

## Run Locally (with venv)
```bash
# Create virtual env
python -m venv .venv
source .venv/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Run app
flask --app app run
```
Visit: http://localhost:5000

## Run with Docker

```bash
# Start the app
docker-compose up

# Stop the app
docker-compose down
```
Visit: http://localhost:5000

# Database Configuration

This project uses PostgreSQL with SQLAlchemy as ORM.

Database settings are configured via .env file:
```
DB_USER=your_db_name
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
DB_HOST=db
DB_PORT=5432
```

You can customize these as needed. The db service in docker-compose.yml will create the database automatically.

## First-time Setup with SQLAlchemy

To begin using the database with your own models (e.g., a MusicAlbum table):

## 1. Create your models

Define your SQLAlchemy models inside app/models.py, for example:
```py
from app import db

class MusicAlbum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
```

## 2. Initialize database (tables)

If you're not using Flask-Migrate yet (migrations), you can simply do:
```commandline
docker-compose exec web flask shell
```

Inside the shell:
```commandline
from app import db
db.create_all()
```

That will create all tables in the connected Postgres DB.

## Optional: Database Migrations with Flask-Migrate

This project includes Flask-Migrate for database version control.
It allows you to update database schema safely as models evolve.

## 1. Initialize migrations (only once):

```commandline
docker-compose exec web flask db init
```

##  2. After changing or adding models:

```commandline
docker-compose exec web flask db migrate -m "Describe your changes"
docker-compose exec web flask db upgrade
```

This will generate and apply Alembic migrations inside the migrations/ directory.

You can use this instead of db.create_all() once migrations are initialized.