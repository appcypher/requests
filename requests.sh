# Add some strict rules to bash
set -euo pipefail

# Where execution starts
main() {
    case $1 in
        build )
            build
        ;;
        cleanup )
            cleanup
        ;;
        --help|help|-h )
            help
        ;;
    esac

    exit 0
}

# Prints helpful information about the requests script
help() {
    echo ""
    echo " ======================|| REQUESTS ||========================"
    echo "|                                                            |"
    echo "|   ∙• A simple utility for managing requests project •∙     |"
    echo "|                                                            |"
    echo "| USAGE:  sh requests.sh [OPTIONS]                           |"
    echo "|                                                            |"
    echo "| OPTIONS:                                                   |"
    echo "|                                                            |"
    echo "|  • help       - prints this help message                   |"
    echo "|  • build      - builds project                             |"
    echo "|  • start      - starts the server                          |"
    echo "|  • cleanup    - removes build dependencies                 |"
    echo "|                                                            |"
    echo " ============================================================"
    echo ""
}

# Sets needed environment variables
setenv() {
    echo "[requests]: setting environment variables"

    # The following lines are needed to prevent pipenv from throwing unknown-locale error
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
}

# Installs necessary dependencies and sets the environmeny
build() {
    echo "[requests]: building project"

    # Install pipenv using pip3
    pip3 install pipenv

    # Install npm dependencies
    npm install

    # Bundle js files
    npm run build:prod

    # Set env variables
    setenv

    # Install pipenv dependecies
    pipenv install

    # Activate virtual env
    pipenv shell

    # Apply migrations
    flask db upgrade -d server/migrations

    # Add seeds to database
    flask model seed all
}

# Starts the server
start() {
    echo "[requests]: starting flask app"

    # Disable all ports except 5000
    sudo ufw enable && sudo ufw allow 5000

    # Set env variables
    setenv

    # Activate virtual environment
    pipenv shell

    # Start wsgi server
    gunicorn --workers 2 manage:flask_app -b 127.0.0.1:5000
}

# Removes projects build dependencies
cleanup() {
    echo "[requests]: cleaning up project installations"

    # Remove node_modules folder
    rm -rf node_modules/

    # Clear pipenv cache
    pipenv --rm

    # Uninstall all packages
    pipenv uninstall --all
}

# Run script
main $1
