import click
import datetime
from collections import Counter
import random
from notes.db import get_notes
from notes.utils.formatting import render_notes_table, console
from notes.utils.text import get_word_count, extract_tags
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel

@click.group()
def info():
    """Insights and Analytics Commands."""
    pass

@info.command()
def insights():
    """Show analytics and insights on your notes."""
    notes = get_notes()
    if not notes:
        console.print("[cyan]No notes yet to analyze.[/cyan]")
        return
        
    total_notes = len(notes)
    all_content = " ".join([n['content'] for n in notes]).lower()
    total_words = sum(get_word_count(n['content']) for n in notes)
    
    # Calculate tags
    all_tags = []
    for note in notes:
        if note['tags']:
            all_tags.extend([t.strip() for t in note['tags'].split(",") if t.strip()])
        all_tags.extend(extract_tags(note['content']))
    
    tag_counter = Counter(all_tags)
    top_tags = tag_counter.most_common(5)
    
    # Calculate words (naive approach, skipping small words)
    words = [w for w in all_content.split() if w.isalnum() and len(w) > 4]
    word_counter = Counter(words)
    top_words = word_counter.most_common(5)
    
    table = Table(title="Notebook Insights", show_header=False)
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value")
    
    table.add_row("Total Notes", str(total_notes))
    table.add_row("Total Words", str(total_words))
    table.add_row("Top Tags", ", ".join([f"{t[0]} ({t[1]})" for t in top_tags]) if top_tags else "None")
    table.add_row("Top Words", ", ".join([f"{w[0]} ({w[1]})" for w in top_words]) if top_words else "None")
    
    console.print(table)


@info.command()
@click.argument('period', type=click.Choice(['day', 'week', 'month']), default='week')
def replay(period):
    """Memory replay: Show notes from the past."""
    now = datetime.datetime.now()
    if period == 'day':
        delta = datetime.timedelta(days=1)
    elif period == 'week':
        delta = datetime.timedelta(days=7)
    elif period == 'month':
        delta = datetime.timedelta(days=30)
        
    target_date = now - delta
    str_target = target_date.strftime("%Y-%m-%d %H:%M:%S")
    
    notes = get_notes()
    past_notes = [n for n in notes if n['created_at'] >= str_target]
    
    if not past_notes:
        console.print(f"[cyan]No notes found from the last {period}.[/cyan]")
        return
        
    console.print(f"[bold magenta]Memory Replay (Last {period.capitalize()})[/bold magenta]")
    
    # Pick a few random notes to replay
    sample_size = min(3, len(past_notes))
    replay_notes = random.sample(past_notes, sample_size)
    
    for note in replay_notes:
        console.print(f"\n[bold]--- from {note['created_at'][:10]} ---[/bold]")
        console.print(note['content'])
        console.print("[dim]-" * 30 + "[/dim]")


@info.command()
def dashboard():
    """Show your daily dashboard."""
    notes = get_notes()
    today_str = datetime.date.today().isoformat()
    
    today_notes = [n for n in notes if n['created_at'][:10] == today_str]
    moods = [n['mood'] for n in today_notes if n['mood']]
    
    mood_summary = Counter(moods).most_common(3) if moods else []
    
    panels = []
    
    p1 = Panel(str(len(today_notes)), title="Notes Today", style="green", padding=(1, 5))
    panels.append(p1)
    
    mood_text = "\n".join([f"{m[0]}: {m[1]}" for m in mood_summary]) if mood_summary else "No moods recorded today"
    p2 = Panel(mood_text, title="Moods Today", style="blue")
    panels.append(p2)
    
    tag_counter = Counter()
    for note in today_notes:
        if note['tags']:
            tag_counter.update([t.strip() for t in note['tags'].split(",") if t.strip()])
    
    top_tags = tag_counter.most_common(3)
    tag_text = "\n".join([f"{t[0]}: {t[1]}" for t in top_tags]) if top_tags else "No tags used today"
    p3 = Panel(tag_text, title="Top Tags Today", style="magenta")
    panels.append(p3)
    
    console.print("[bold yellow]Daily Dashboard[/bold yellow]")
    console.print(Columns(panels))
