#!/bin/bash

rm -f db.sqlite3
rm expert/fixtures/initial_data.json

python manage.py syncdb --noinput
python manage.py createsuperuser --username=jackon --email=jiekunyang@gmail.com

python manage.py check_permissions  # required by userena

git checkout expert/fixtures/initial_data.json

python manage.py loaddata expert/fixtures/initial_data.json

rm -rf media
cp -R init_data media
