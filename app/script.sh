#!/bin/sh

# Set app service root directory
#export APPDIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
# Set virtual environment path
VENVPATH="${APPDIR}/${VENV}"
export FLASK_APP="${APPDIR}/src/app.py"
# Updating the PATH with project's-specific bin folders
export PATH=$HOME/.local/bin:$VENVPATH/bin:$PATH

# Automate the VENV path folder and environment creation
create_env() {
    echo "Creating virtual environment"
    python3 -m venv "${VENVPATH}"
}

# Use entrypoint.sh to run the app with whatever command you need
run() {
    "${APPDIR}"/entrypoint.sh
}

# Aliases
alias activate=". activate"

# Create the VENV if doesn't exists
if [ ! -d "${VENVPATH}" ]; then
    create_env
fi

# If the VENV has been created but it is not activated, activate it
if  [ -d "${VENVPATH}" ] && [ -z "${VIRTUAL_ENV}" ]; then
. activate
fi