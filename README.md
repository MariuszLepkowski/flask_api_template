# Recruitment Task – Flask REST API

This is a recruitment REST API task built with Flask by Mariusz Łepkowski.  
It supports both local setup via virtual environment and Docker.

- Flask + RESTful architecture
- Input/output via JSON
- Ready for unit testing
- Minimal structure, easy to extend

---

## Requirements

- Python 3.10+
- (Optional) Docker

## Run Locally (with venv)

```bash
# Clone the repo
git clone https://github.com/youruser/recruitment-api-template.git
cd recruitment-api-template

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

