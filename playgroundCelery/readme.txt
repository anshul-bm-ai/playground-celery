How to run celery?
Install
pip3 install django_celery_results

Add 
CELERY_RESULT_BACKEND = 'django-db'
To settings.py

To activate celery we need to run a worker
Run it in a screen and inside a project directory
screen -L -S worker
celery -A <your project name> worker -S django
ctrl + A + wait + D

Then start shell and try celery.





