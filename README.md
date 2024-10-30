# Gettings Started
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver localhost:8000
```

# Create a new migration
python manage.py makemigrations

# Apply the migration to update the database schema
python manage.py migrate

# Goals

[x] Get Groups perm & display
[x] Top menu bar
[ ] UI Theming
[ ] UI theming controlled via conf file (light and dark mode for UW, for personal, for church)
[x] Role based menus
[ ] Subnetcalc page honoring UI theming
[x] Sidebar
[ ] Footer
