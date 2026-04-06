import click
import json
import datetime
from rich.console import Console
from notes.db import get_notes, get_connection

console = Console()

@click.group()
def data():
    """Import and export data."""
    pass

@data.command(name='export')
@click.option('--format', 'fmt', type=click.Choice(['json', 'md']), default='json', help='Export format (json or md)')
@click.option('--file', 'filename', type=str, help='Output filename')
def export_notes(fmt, filename):
    """Export all notes to a file."""
    notes = get_notes(order_by="id ASC")
    if not notes:
        console.print("[yellow]No notes to export.[/yellow]")
        return
        
    # Convert rows to dicts
    notes_list = [dict(row) for row in notes]
    
    if fmt == 'json':
        out_file = filename or f"notes_export_{datetime.datetime.now().strftime('%Y%m%d')}.json"
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(notes_list, f, indent=4)
        console.print(f"[green]Successfully exported {len(notes)} notes to {out_file}[/green]")
        
    elif fmt == 'md':
        out_file = filename or f"notes_export_{datetime.datetime.now().strftime('%Y%m%d')}.md"
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write("# Notes Export\n\n")
            for note in notes_list:
                f.write(f"## Note {note['id']} - {note['created_at']}\n")
                if note['tags']:
                    f.write(f"**Tags:** {note['tags']} | ")
                if note['mood']:
                    f.write(f"**Mood:** {note['mood']}")
                f.write("\n\n")
                f.write(f"{note['content']}\n\n")
                f.write("---\n\n")
        console.print(f"[green]Successfully exported {len(notes)} notes to {out_file}[/green]")

@data.command(name='import')
@click.argument('filename', type=click.Path(exists=True))
def import_notes(filename):
    """Import notes from a JSON file."""
    if not filename.endswith('.json'):
        console.print("[red]Only JSON imports are currently supported.[/red]")
        return
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            notes_data = json.load(f)
            
        if not isinstance(notes_data, list):
            console.print("[red]Invalid JSON format. Expected a list of notes.[/red]")
            return
            
        conn = get_connection()
        c = conn.cursor()
        count = 0
        for note in notes_data:
            content = note.get('content')
            if not content:
                continue
            tags = note.get('tags', '')
            category = note.get('category', '')
            mood = note.get('mood', '')
            is_fav = note.get('is_favorite', 0)
            created = note.get('created_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            updated = note.get('updated_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            c.execute(
                "INSERT INTO notes (content, tags, category, mood, is_favorite, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (content, tags, category, mood, is_fav, created, updated)
            )
            count += 1
            
        conn.commit()
        conn.close()
        console.print(f"[green]Successfully imported {count} notes from {filename}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error importing notes: {str(e)}[/red]")
