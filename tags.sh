#!/bin/bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon varianti

python manage.py auto_tag --generate=100 --assign --settings=settings.settings