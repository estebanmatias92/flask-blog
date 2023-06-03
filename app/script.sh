#!/bin/sh

# Re-export the VIRTUAL_ENV var
export VIRTUAL_ENV="${APPDIR}/venv"
# Add the VENV bin folder to PATH
export PATH="${VIRTUAL_ENV}/bin:${PATH}"

# Use entrypoint.sh to run the app with whatever command you need
run() {
    ${APPDIR}/entrypoint.sh
}

# Create the VENV if doesn't exists
if [ ! -d "${VIRTUAL_ENV}" ]; then
    echo "Creating virtual environment"
    python3 -m venv "${VIRTUAL_ENV}"
fi
