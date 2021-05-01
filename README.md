# tutor
tutor registration and test project

To run project follow these steps-

- install python on your machine (you can skip this step if already have)
- install pip (you can skip this step if already have)
- clone this project
- $ cd tutor (you can make any other folder name)
- create virtual environment $pip install virtualenv (you can skip this step if already have virtualenv)
- $virtualenv venv, $source venv/bin/activate (use 'work on venv' if on windows)
- $ python -m pip install Django
- $ pip install pillow
- $ install and configure mysql pkg if not using sqlite
- $ python manage.py makemigrations
- $ python manage.py migrate 
- $ python manage.py createsuperuser 
- $ python manage.py runserver
