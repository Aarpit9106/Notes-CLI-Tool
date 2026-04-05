import click
import sys
from notes.db import add_note, get_notes, get_note, update_note, delete_note
from notes.utils.formatting import print_success, print_error, render_notes_table, render_note, console

@click.group()
def core():
    """Core note-taking commands."""
    pass

@core.command()
@click.argument('content', required=False)
@click.option('--tag', '-t', help="Tags for the note (comma-separated)", default="")
@click.option('--category', '-c', help="Category for the note", default="")
@click.option('--mood', '-m', help="Your mood", default="")
@click.option('--favorite', is_flag=True, help="Mark as favorite")
def add(content, tag, category, mood, favorite):
    """Add a new note."""
    if not content:
        content = click.edit("Enter your note here. Markdown is supported.")
        if not content or not content.strip():
            print_error("Note content cannot be empty.")
            return

    note_id = add_note(content.strip(), tag, category, mood, 1 if favorite else 0)
    print_success(f"Note added with ID {note_id}")

@core.command(name='list')
@click.option('--limit', '-l', type=int, default=50, help="Number of notes to show")
def list_notes(limit):
    """List recent notes."""
    notes = get_notes(limit=limit)
    render_notes_table(notes, title="Recent Notes")

@core.command()
@click.argument('note_id', type=int)
def view(note_id):
    """View a specific note."""
    note = get_note(note_id)
    if not note:
        print_error(f"No note found with ID {note_id}")
        return
    render_note(note)

@core.command()
@click.argument('note_id', type=int)
@click.option('--tag', '-t', help="New tags", default=None)
@click.option('--category', '-c', help="New category", default=None)
@click.option('--mood', '-m', help="New mood", default=None)
@click.option('--favorite/--no-favorite', default=None, help="Update favorite status")
def edit(note_id, tag, category, mood, favorite):
    """Edit an existing note."""
    note = get_note(note_id)
    if not note:
        print_error(f"No note found with ID {note_id}")
        return

    updates = {}
    if tag is not None:
        updates['tags'] = tag
    if category is not None:
        updates['category'] = category
    if mood is not None:
        updates['mood'] = mood
    if favorite is not None:
        updates['is_favorite'] = 1 if favorite else 0

    # If no flags provided, edit the content
    if not updates:
        new_content = click.edit(note['content'])
        if new_content and new_content.strip() != note['content']:
            updates['content'] = new_content.strip()
        else:
            print_error("No changes made.")
            return

    if update_note(note_id, **updates):
        print_success(f"Note {note_id} updated.")
    else:
        print_error(f"Failed to update note {note_id}.")

@core.command()
@click.argument('note_id', type=int)
def delete(note_id):
    """Delete a note."""
    if delete_note(note_id):
        print_success(f"Note {note_id} deleted.")
    else:
        print_error(f"No note found with ID {note_id} or failed to delete.")

@core.command()
@click.option('--tag', '-t', help="Tags to apply to all dump notes", default="")
@click.option('--category', '-c', help="Category for all dump notes", default="")
def dump(tag, category):
    """Brain dump mode. Keep entering notes sequentially using empty lines or Ctrl+D to stop."""
    console.print("[bold cyan]Brain Dump Mode[/bold cyan] started.")
    console.print("Type your notes. Press Enter twice to save the current note and start a new one. Press Ctrl+D (or Ctrl+Z on Windows) to exit.")
    
    current_content = []
    
    try:
        while True:
            try:
                line = input()
                if line == "":
                    # Empty line implies end of current note if there is content
                    if current_content:
                        content = "\n".join(current_content)
                        note_id = add_note(content, tag, category, "focused", 0)
                        print_success(f"Saved note {note_id}")
                        current_content = []
                else:
                    current_content.append(line)
            except EOFError:
                if current_content:
                    content = "\n".join(current_content)
                    note_id = add_note(content, tag, category, "focused", 0)
                    print_success(f"Saved note {note_id}")
                break
    except KeyboardInterrupt:
        pass
    
    console.print("\n[bold cyan]Exited Brain Dump Mode.[/bold cyan]")
