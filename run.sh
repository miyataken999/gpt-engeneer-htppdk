#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the Django application
python project/manage.py runserver
