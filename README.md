# Swagger with Django REST Framework

Integration of Swagger with DRF to generate API documentation.

## Getting Started

Works on **Python 3+** and **Django 3+**.

1. Install dependencies:

```
python -m pip install -r requirements.txt
```

2. Run migrations & start the server:

```
python manage.py migrate
python manage.py runserver
```

## Testing

Navigate below URL to view docs .

```
localhost:8000/api/v1/swagger/schema
```
