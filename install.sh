#!/bin/bash

rm -f db.sqlite3
mv expert/fixtures/initial_data.json t1.json
mv std_product/fixtures/initial_data.json t2.json
mv provider/fixtures/initial_data.json t3.json

python manage.py syncdb --noinput
python manage.py createsuperuser --username=jackon --email=jiekunyang@gmail.com

python manage.py check_permissions  # required by userena

mv t1.json expert/fixtures/initial_data.json
mv t2.json std_product/fixtures/initial_data.json
mv t3.json provider/fixtures/initial_data.json

python manage.py loaddata expert/fixtures/initial_data.json

rm -rf media
cp -R init_data media
