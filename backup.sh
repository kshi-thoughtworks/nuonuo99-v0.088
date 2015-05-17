#!/bin/bash

python manage.py dumpdata --indent=4 base > base/fixtures/initial_data.json
python manage.py dumpdata --indent=4 provider > provider/fixtures/initial_data.json
python manage.py dumpdata --indent=4 location> location/fixtures/initial_data.json
python manage.py dumpdata --indent=4 expert > expert/fixtures/initial_data.json

rm -rf init_data
cp -R media init_data
