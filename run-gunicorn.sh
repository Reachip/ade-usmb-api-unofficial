#!/bin/sh

pip install -r requirements
gunicorn --bind=0.0.0.0:80 --workers=3 wsgi:app