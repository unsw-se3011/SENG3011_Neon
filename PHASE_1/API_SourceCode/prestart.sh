#! /usr/bin/env bash

sleep 10

./manage.py migrate 
./manage.py loaddata data.json
