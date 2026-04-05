import click
from notes.db import init_db
from notes.commands.core import core
from notes.commands.organize import organize
from notes.commands.future import future, check_future_messages
from notes.commands.insights import info

@click.group()
def cli():
    """Notes CLI - Your Second Brain in the Terminal."""
    # Ensure database is initialized
    init_db()
    # Check for delivery of future messages before any command
    check_future_messages()

# Add command groups and commands
cli.add_command(core.commands['add'], name="add")
cli.add_command(core.commands['list'], name="list")
cli.add_command(core.commands['view'], name="view")
cli.add_command(core.commands['edit'], name="edit")
cli.add_command(core.commands['delete'], name="delete")
cli.add_command(core.commands['dump'], name="brain-dump")

# Add organize commands
cli.add_command(organize.commands['search'], name="search")
cli.add_command(organize.commands['link'], name="link")
cli.add_command(organize.commands['links'], name="links")
cli.add_command(organize.commands['mood'], name="mood")

# Add future command group
cli.add_command(future.commands['send'], name="send-future")

# Add insights commands
cli.add_command(info.commands['insights'], name="insights")
cli.add_command(info.commands['replay'], name="replay")
cli.add_command(info.commands['dashboard'], name="dashboard")

if __name__ == '__main__':
    cli()
