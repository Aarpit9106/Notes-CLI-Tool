# 🧠 Notes CLI Tool

> A powerful, keyboard-driven **Second Brain** for taking, organizing, and retrieving notes directly from your terminal.

Built with **Python + Click + Rich + SQLite**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![CLI](https://img.shields.io/badge/interface-CLI-black.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

# ✨ Features

* 🧩 **Core Note Management**: Add, list, view, edit, and delete notes rapidly.
* 🏷️ **Organization**: Tag your notes, filter by tags, and use the rapid search functionality.
* 😊 **Mood Tracking**: Record mood with notes and track productivity trends.
* 📊 **Insights & Dashboard**: View a daily dashboard, top tags, most used words, and productivity analytics.
* ⏳ **Future Messages**: Send notes to your future self that deliver on a specified date.
* 🔗 **Knowledge Graph Linking**: Link notes together to create a true second brain style knowledge network.
* 🧠 **Brain Dump Mode**: Continuous thought capture—perfect for journaling, idea capture, or thinking sessions.
* 💾 **Data Portability**: Native export/import functionality to safely backup and transfer your notes database.

---

# 🚀 Quick Start

The fastest way to get started is to use the standalone executable or install via `pip`.

### Option 1 — Download EXE (Recommended, No Python Required)
If you don't have Python installed, you can simply download the pre-compiled `.exe` file. Head to the **[Releases](../../releases)** page to download the latest binary. 

### Option 2 — pip install (For Python Users)
```bash
git clone https://github.com/Aarpit9106/Notes-CLI-Tool.git
cd Notes-CLI-Tool
pip install -e .
notes --help
```

---

# 📥 Run using EXE (No Python required)

No Python? No problem. Use the standalone binary:

**Step 1:** Go to the [GitHub Releases](../../releases) page.
**Step 2:** Download the `notes-windows.exe` file.
**Step 3:** Open a terminal (PowerShell/Command Prompt) in your download folder.
**Step 4:** Run it to see the help menu:
```bash
.\notes-windows.exe --help
```
**Step 5:** Try adding a note:
```bash
.\notes-windows.exe add "hello"
.\notes-windows.exe list
```
**Step 6 (Optional):** Rename the file to `notes.exe` for easier typing:
```bash
notes add "idea"
```

---

# 📦 Run using pip install

If you have Python 3.8+ installed, using `pip` makes the `notes` command available globally anywhere on your system.

```bash
git clone https://github.com/Aarpit9106/Notes-CLI-Tool.git
cd Notes-CLI-Tool
pip install -e .
```

Now you can just type `notes` from any folder!

---

# 🛠️ Run from source (developers)

If you're a developer wanting to modify the tool:

```bash
git clone https://github.com/Aarpit9106/Notes-CLI-Tool.git
cd Notes-CLI-Tool
pip install -r requirements.txt
python main.py --help
```

---

# ⌨️ CLI Commands

| Command | Description |
|---|---|
| `notes add` | add note |
| `notes list` | list notes |
| `notes view` | view a specific note |
| `notes edit` | edit an existing note |
| `notes delete`| delete a note |
| `notes search`| search notes |
| `notes mood` | filter notes by mood |
| `notes dashboard` | show dashboard |
| `notes insights`| analytics |
| `notes brain-dump` | capture ideas |
| `notes link` | connect notes |
| `notes links` | view links for a note |
| `notes send-future`| send a note to yourself |
| `notes replay` | replay your memories |
| `notes export` | export data to JSON/Markdown |
| `notes import` | import data from JSON |

---

# 💡 Examples

Adding a simple idea:
```bash
notes add "Startup idea" --tag ideas --mood creative
```

Viewing your recent notes:
```bash
notes list
```

Checking your daily dashboard summary:
```bash
notes dashboard
```

Linking notes to create a knowledge graph:
```bash
notes link 1 2
```

---

# 🖼️ Screenshots (ASCII ok)

```text
Daily Dashboard
╭───── Notes Today ─────╮ ╭────── Moods Today ──────╮ ╭── Top Tags Today ──╮
│                       │ │ creative: 1             │ │ ideas: 2           │
│     3                 │ ╰─────────────────────────╯ ╰────────────────────╯
│                       │
╰───────────────────────╯
```

---

# 📁 Project Structure

```
Notes-CLI-Tool
│
├── notes/
│   ├── commands/
│   ├── db.py
│   └── cli.py
├── .github/
│   └── workflows/
├── requirements.txt
├── pyproject.toml
├── main.py
└── README.md
```

---

# ⚙️ How it works

The CLI uses **Click** to route user commands, processing arguments and options (like tags, dates, and moods) seamlessly. The data is managed persistently on your local machine using **SQLite**, meaning your notes are queryable, portable, and entirely private. All output is styled elegantly using **Rich** to provide a readable, keyboard-friendly terminal interface. Best of all, a native GitHub Actions pipeline creates automated `.exe` builds on release for ultimate distribution.

---

# 🔧 Troubleshooting

### `notes` command not found
If the command isn't recognized, your Python package paths might not be loaded, or it wasn't installed correctly. Run this from within the tool's folder:
```bash
pip install -e .
```

### `exe not running`
When running the downloaded executable on Windows without adding it to your `PATH`, you must explicitly point to the current directory:
```bash
.\notes.exe
```

### `database reset`
If you ever want to completely restart, just delete the local SQLite database file:
- On Windows: `del ~/.notes_cli.db`
- On Mac/Linux: `rm ~/.notes_cli.db`

---

# 🗺️ Roadmap

* [x] Export/Import notes
* [x] GitHub Actions automated binary releases
* [ ] Cloud sync optionally
* [ ] AI summarization
* [ ] Web UI or Mobile companion
* [ ] Plugin system

---

# 👨‍💻 Author

Built by **Aarpit Jethwa**
GitHub: [https://github.com/Aarpit9106](https://github.com/Aarpit9106)

---

# 📄 License

This project is licensed under the MIT License.
