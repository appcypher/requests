from click.testing import CliRunner
from cli import seed_model
from flask.cli import ScriptInfo
from models import (Client, Staff, Comment, Request)


def test_flask_seed_model_cli_seeds_to_db_with_all_option(cli_app):
    """
    Tests that db tables are populated `flask seed model` when passed an `all`
    option.

    Args:
        cli_app (function): a flask app factory function that also manages its
            context.
    """
    # Create a script for running application.
    obj = ScriptInfo(create_app=cli_app)

    # Call command, apply arguments and create app.
    result = CliRunner().invoke(seed_model, ['all'], obj=obj)

    clients = Client.get_all()
    staff = Staff.get_all()
    requests = Request.get_all()
    comments = Comment.get_all()

    assert len(clients) == 3
    assert len(staff) == 3
    assert len(comments) == 14
    assert len(requests) == 12
    assert result.exit_code == 0


def test_flask_seed_model_cli_seeds_to_db_with_client_option(cli_app):
    """
    Tests that client table is populated `flask seed model` when passed a
    `client` option.

    Args:
        cli_app (function): a flask app factory function that also manages its
            context.
    """
    # Create a script for running application.
    obj = ScriptInfo(create_app=cli_app)

    # Call command, apply arguments and create app.
    result = CliRunner().invoke(seed_model, ['client'], obj=obj)

    clients = Client.get_all()

    assert len(clients) == 3
    assert result.exit_code == 0


def test_flask_seed_model_cli_seeds_to_db_with_staff_option(cli_app):
    """
    Tests that staff table is populated `flask seed model` when passed a
    `staff` option.

    Args:
        cli_app (function): a flask app factory function that also manages its
            context.
    """
    # Create a script for running application.
    obj = ScriptInfo(create_app=cli_app)

    # Call command, apply arguments and create app.
    result = CliRunner().invoke(seed_model, ['staff'], obj=obj)

    staffs = Staff.get_all()

    assert len(staffs) == 3
    assert result.exit_code == 0


def test_flask_seed_model_cli_seeds_to_db_with_comment_option(
    cli_app, multiple_valid_request_models
):
    """
    Tests that comment table is populated `flask seed model` when passed a
    `comment` option.

    Args:
        cli_app (function): a flask app factory function that also manages its
            context.
    """
    # Create a script for running application.
    obj = ScriptInfo(create_app=cli_app)

    # Call command, apply arguments and create app.
    result = CliRunner().invoke(seed_model, ['comment'], obj=obj)

    comments = Comment.get_all()

    assert len(comments) == 14
    assert result.exit_code == 0


def test_flask_seed_model_cli_seeds_to_db_with_request_option(
    cli_app, multiple_valid_client_models, multiple_valid_staff_models
):
    """
    Tests that request table is populated `flask seed model` when passed a
    `request` option.

    Args:
        cli_app (function): a flask app factory function that also manages its
            context.
    """
    # Create a script for running application.
    obj = ScriptInfo(create_app=cli_app)

    # Call command, apply arguments and create app.
    result = CliRunner().invoke(seed_model, ['request'], obj=obj)

    requests = Request.get_all()

    assert len(requests) == 12
    assert result.exit_code == 0
