import click
import datetime
from notes.db import add_future_message, get_undelivered_future_messages, mark_future_message_delivered
from notes.utils.formatting import print_success, print_error, print_info, console
from rich.panel import Panel

@click.group()
def future():
    """Future messaging capabilities."""
    pass

@future.command(name="send")
@click.argument('content')
@click.option('--date', '-d', required=True, help="Date to show the message (YYYY-MM-DD)")
def send_future(content, date):
    """Send a note to your future self."""
    try:
        # Validate date
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print_error("Invalid date format. Use YYYY-MM-DD.")
        return

    add_future_message(content, date)
    print_success(f"Message scheduled for {date}.")

def check_future_messages():
    """Check for and display undelivered messages from the past/today."""
    msgs = get_undelivered_future_messages()
    if not msgs:
        return

    for msg in msgs:
        panel = Panel(msg['content'], title="🚀 Message From The Past", subtitle=f"Initially written: {msg['created_at'][:10]}", border_style="magenta")
        console.print(panel)
        mark_future_message_delivered(msg['id'])
