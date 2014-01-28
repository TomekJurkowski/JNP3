#!/bin/bash
cd /home/JNP3/pychan
python manage.py run_gunicorn --workers=2
