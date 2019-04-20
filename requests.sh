# Add some strict rules to bash
set -eu

# Where execution starts
main() {
    case $1 in
        build )
            build
        ;;
        start )
            start
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
set_env_vars() {
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

    # Set locale environmwnt variables
    set_env_vars

    # Install pipenv dependecies
    pipenv install --dev
}

# Starts the server
start() {
    echo "[requests]: starting flask app"

    # Set locale environmwnt variables
    set_env_vars

    # Activate virtual environment and start wsgi server.
    pipenv run gunicorn --pythonpath ./server --workers 2 manage:flask_app -b 0.0.0.0:5000
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
