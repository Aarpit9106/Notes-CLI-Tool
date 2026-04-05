from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def print_error(msg):
    console.print(f"[bold red]Error:[/bold red] {msg}")

def print_success(msg):
    console.print(f"[bold green]Success:[/bold green] {msg}")

def print_info(msg):
    console.print(f"[bold cyan]Info:[/bold cyan] {msg}")

def print_warning(msg):
    console.print(f"[bold yellow]Warning:[/bold yellow] {msg}")

def render_notes_table(notes, title="Notes"):
    if not notes:
        print_info("No notes found.")
        return

    table = Table(title=title, show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Content Snippet", min_width=30)
    table.add_column("Tags")
    table.add_column("Category")
    table.add_column("Mood")
    table.add_column("Fav", justify="center")
    table.add_column("Updated", style="dim")

    for note in notes:
        snippet = note['content'].split('\n')[0]
        if len(snippet) > 50:
            snippet = snippet[:47] + "..."
        
        fav = "⭐" if note['is_favorite'] else ""
        table.add_row(
            str(note['id']),
            snippet,
            note['tags'] or "",
            note['category'] or "",
            note['mood'] or "",
            fav,
            note['updated_at'][:10]
        )

    console.print(table)

def render_note(note):
    if not note:
        print_error("Note not found.")
        return
    
    header = f"[bold]Note ID:[/bold] {note['id']} | [bold]Tags:[/bold] {note['tags'] or 'None'} | [bold]Category:[/bold] {note['category'] or 'None'}"
    if note['mood']:
        header += f" | [bold]Mood:[/bold] {note['mood']}"
    if note['is_favorite']:
        header += " | ⭐ [bold yellow]Favorite[/bold yellow]"
        
    header += f"\n[dim]Created: {note['created_at']} | Updated: {note['updated_at']}[/dim]"
    
    md = Markdown(note['content'])
    panel = Panel(md, title=f"Note {note['id']}", subtitle=header, border_style="blue")
    console.print(panel)
