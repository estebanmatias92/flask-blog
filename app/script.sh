#!/bin/sh

# Re-export the VIRTUAL_ENV var
export VIRTUAL_ENV="${APPDIR}/venv"

# Use entrypoint.sh to run the app with whatever command you need
run() {
    (. $VIRTUAL_ENV/bin/activate; ${APPDIR}/entrypoint.sh)
}

# Create the VENV if doesn't exists
if [ ! -d "${VIRTUAL_ENV}" ]; then
    echo "Creating virtual environment"
    python3 -m venv "${VIRTUAL_ENV}"
fi