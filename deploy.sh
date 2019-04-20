# Add some strict rules to bash
set -eu

# Where execution starts
main() {
    case $1 in
        create )
            create
        ;;
        automate )
            automate
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
    echo "|  • create     - creates ECS cluster and service            |"
    echo "|  • automate   - start a CodePipeline                       |"
    echo "|                                                            |"
    echo " ============================================================"
    echo ""
}

create() {
    echo "[deploy]: creating ECS cluster and services"
}


# Run script
main $1
