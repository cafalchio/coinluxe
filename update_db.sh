#!/bin/bash

cd /home/cafalchio/Projects/coinluxe
source .venv/bin/activate

python manage.py update_coins
python manage.py update_coins_details
python manage.py update_coins_charts
python manage.py update_coins --save_pics True
python manage.py create_stripe_products
