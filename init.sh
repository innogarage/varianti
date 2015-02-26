#!/bin/bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon varianti

python manage.py syncdb --settings=settings.settings
python manage.py migrate tema.links --settings=settings.settings