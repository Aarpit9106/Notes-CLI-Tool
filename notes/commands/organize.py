import click
from notes.db import search_notes, link_notes, get_note, get_linked_notes
from notes.utils.formatting import print_success, print_error, render_notes_table, render_note

@click.group()
def organize():
    """Commands for organizing and searching notes."""
    pass

@organize.command()
@click.argument('keyword', default="")
@click.option('--tag', '-t', help="Search by tag", default="")
@click.option('--category', '-c', help="Search by category", default="")
@click.option('--mood', '-m', help="Search by mood", default="")
@click.option('--date', '-d', help="Search by date (YYYY-MM-DD)", default="")
def search(keyword, tag, category, mood, date):
    """Search your notes."""
    notes = search_notes(keyword, tag, category, date, mood)
    if not notes:
        print_error("No notes found matching criteria.")
    else:
        render_notes_table(notes, title="Search Results")

@organize.command()
@click.argument('id1', type=int)
@click.argument('id2', type=int)
def link(id1, id2):
    """Link two notes together."""
    if not get_note(id1) or not get_note(id2):
        print_error("One or both note IDs do not exist.")
        return
    
    if link_notes(id1, id2):
        print_success(f"Linked Note {id1} and Note {id2} successfully.")
    else:
        print_error("Failed to link notes.")

@organize.command()
@click.argument('note_id', type=int)
def links(note_id):
    """View connections for a specific note."""
    note = get_note(note_id)
    if not note:
        print_error(f"Note {note_id} not found.")
        return
        
    linked = get_linked_notes(note_id)
    if not linked:
        print_error(f"Note {note_id} has no linked notes.")
        return
        
    render_notes_table(linked, title=f"Notes linked to {note_id}")

@organize.command()
@click.argument('mood_name')
def mood(mood_name):
    """Filter notes by mood."""
    notes = search_notes(mood=mood_name)
    if not notes:
        print_error(f"No notes found with mood '{mood_name}'.")
    else:
        render_notes_table(notes, title=f"Mood: {mood_name.capitalize()}")
