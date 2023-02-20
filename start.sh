#!/usr/bin/env bash

cd /root/dashboard

export FLASK_APP=app
export FLASK_ENV=production

python3 -m flask run --host=0.0.0.0 --port=80
