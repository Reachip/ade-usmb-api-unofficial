#!/bin/sh

gunicorn --bind=0.0.0.0:80 --workers=3 wsgi:app