"""
Database setup script to create migrations and apply them.
Run this from the project root: python manage.py shell < scripts/setup_db.py
"""
import os
import sys
import django
from django.core.management import call_command

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

print("[v0] Starting database setup...")

# Create migrations for the jobs app
print("[v0] Creating migrations for jobs app...")
call_command('makemigrations', 'jobs')

# Apply all migrations
print("[v0] Applying migrations...")
call_command('migrate')

print("[v0] Database setup complete!")
print("[v0] You can now:")
print("[v0]   1. Create a superuser: python manage.py createsuperuser")
print("[v0]   2. Run the server: python manage.py runserver")
