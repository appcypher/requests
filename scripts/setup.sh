#! /bin/sh

# TODO; Check for failure
main() {
    # Clone repository
    git clone https://www.github.com/appcypher/feature-request.git

    # Cd into repostiory
    cd feature-request

    # Install pipenv using pip3
    pip3 install pipenv

    # Install pipenv dependecies
    pipenv install

    # Install npm dependencies
    npm install

    # Bundle js files
    npm run build:prod:dev

    # Apply migrations
    flask db upgrade -d server/migrations
}

main
