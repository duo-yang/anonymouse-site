#!/bin/sh

killall flask

if [ ! -e env ]; then
	python -m venv env
fi

if [ -z ${BROWSER+x} ]; then
	BROWSER="firefox"
fi

source env/bin/activate
export FLASK_APP=main
export FLASK_ENV=development
flask run &
sleep 3
${BROWSER} http://127.0.0.1:5000/
