This project contains website written in Flask which communicates by AJAX with users microservice.
On this site can add/load/removed users and managing site-settings.

## Instalation
Go to project directory and then:
`pip install -r requirements.txt`

## Configuration and Launching
Set enviroment variable USERS_CONFIG with one of values:
 * development - for developing,
 * testing - for run tests,
 * production - on the production server

Then `python manage.py migrate` for run application
or `python manage.py test` run tests.
