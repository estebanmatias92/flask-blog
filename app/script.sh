#!/bin/sh

# Set app service root directory
#export APPDIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
# Set virtual environment path and venv/bin path
VENVPATH="${APPDIR}/${VENV}"
BINPATH="${VENVPATH}/bin"
# Updating the PATH with project's-specific bin folders
#export PATH=$HOME/.local/bin:$PATH

# Automate the VENV path folder and environment creation
create_env() {
    echo "Creating virtual environment"
    python3 -m venv "${VENVPATH}"
}

# Call the envrionment (For dev scripts only)
activate_env() {
   . "${BINPATH}/activate"
}

# Use entrypoint.sh to run the app with whatever command you need
run() {
    (activate_env; ${APPDIR}/entrypoint.sh)
}

# Aliases
alias activate="activate_env"

# Create the VENV if doesn't exists
if [ ! -d "${VENVPATH}" ]; then
    create_env
fi

# If the VENV has been created but it is not activated, activate it
if  [ -d "${VENVPATH}" ] && [ -z "${VIRTUAL_ENV}" ]; then
    activate_env
fi