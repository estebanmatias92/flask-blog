#!/bin/sh

# (TO DO CHANGE)
# Server address 
SERVER_IP="0.0.0.0"
SERVER_PORT="5000"

# Init the app 
if [ "${FLASK_ENV}" = "development" ]; then
    flask run --debug --host=${SERVER_IP} --port=${SERVER_PORT}
else
    flask run --host=${SERVER_IP} --port=${SERVER_PORT}
fi