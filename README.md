# Notes CLI Tool

A powerful, keyboard-driven "Second Brain" CLI for taking, organizing, and finding notes directly from your terminal. Built with Python, Click, Rich, and SQLite.

## Features

- **Core Actions:** Add, list, view, edit, and delete notes.
- **Organization:** Tag your notes and filter them rapidly.
- **Mood Tracking:** Record your mood and see trends over time.
- **Insights & Dashboard:** View analytical statistics (e.g. top words, top tags) and a daily dashboard.
- **Future Messages:** Send notes to your future self that will automatically deliver on a specified date.
- **Linking:** Link notes together to create a knowledge graph structure.
- **Brain Dump Mode:** Enter a continuous stream of thoughts broken into distinct notes.

## Installation

Ensure you have Python 3 installed. Clone this repository and install the dependencies:

```bash
# Clone the repository
git clone https://github.com/Aarpit9106/Notes-CLI-Tool.git
cd Notes-CLI-Tool

# Install the package globally
pip install -e .
```

## Usage

Once installed, the `notes` command is available globally.

### Common Commands

* **Add a note:** `notes add "Buy milk" --tag groceries --mood focused`
* **List notes:** `notes list`
* **View a specific note:** `notes view 1`
* **Edit a note:** `notes edit 1 --tag shopping`
* **Delete a note:** `notes delete 1`

### Organization & Brain Dump

* **Search:** `notes search "milk"`
* **Brain Dump:** `notes brain-dump --tag daily-thoughts`
* **Mood Filter:** `notes mood focused`
* **Link Notes:** `notes link 1 2`
* **View Links:** `notes links 1`

### Advanced Features

* **Insights:** `notes insights`
* **Dashboard:** `notes dashboard`
* **Memory Replay:** `notes replay week`
* **Send to Future:** `notes send-future "Review annual goals" --date 2026-12-31`

## Example Output

### Dashboard
```
Daily Dashboard
╭───── Notes Today ─────╮ ╭────── Moods Today ──────╮ ╭── Top Tags Today ──╮
│                       │ │ creative: 1             │ │ ideas: 2           │
│     3                 │ ╰─────────────────────────╯ ╰────────────────────╯
│                       │
╰───────────────────────╯
```
