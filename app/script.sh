#!/bin/sh

# Re-export the VIRTUAL_ENV var
export VIRTUAL_ENV="${APPDIR}/venv"

# Create the VENV if doesn't exists
if [ ! -d "${VIRTUAL_ENV}" ]; then
    echo "Creating virtual environment"
    python3 -m venv "${VIRTUAL_ENV}"
fi

# Add the venv binaries to the PATH
if ! echo $PATH | grep -q "${VIRTUAL_ENV}/bin:"; then
    echo "Adding venv bin to PATH"
    export PATH="${VIRTUAL_ENV}/bin:${PATH}"
fi

# Use entrypoint.sh to run the app with whatever command you need
run() {
    ${APPDIR}/entrypoint.sh
}