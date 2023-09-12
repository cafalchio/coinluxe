#!/bin/bash

# Navigate to the directory containing your Python script
cd /home/cafalchio/Projects/coinluxe
source .venv/bin/activate

# Run the Python command
python manage.py update_coins
python manage.py update_coins_details
python manage.py update_coins_charts
python manage.py update_prices
python manage.py update_coins --save_pics True