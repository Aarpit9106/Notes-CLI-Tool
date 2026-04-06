# 🧠 Notes CLI Tool

> A powerful, keyboard-driven **Second Brain** for taking, organizing, and retrieving notes directly from your terminal.

Built with **Python + Click + Rich + SQLite**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![CLI](https://img.shields.io/badge/interface-CLI-black.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

# 🎬 Demo

![Notes CLI Demo](demo.gif)

```bash
notes add "Build startup idea" --tag ideas --mood creative
notes list
notes dashboard
notes insights
```

---

# ✨ Features

## 🧩 Core Note Management

* Add, list, view, edit, and delete notes
* Fast keyboard-driven workflow
* Instant CLI access

## 🏷️ Organization

* Tag your notes
* Filter by tags
* Rapid search
* Structured knowledge system

## 😊 Mood Tracking

* Record mood with notes
* Track productivity trends
* Mood-based filtering

## 📊 Insights & Dashboard

* Daily dashboard
* Top tags
* Most used words
* Productivity analytics

## ⏳ Future Messages

Send notes to your future self

```bash
notes send-future "Review annual goals" --date 2026-12-31
```

## 🔗 Knowledge Graph Linking

Link notes together

```bash
notes link 1 2
notes links 1
```

Create a **second brain style knowledge network**

## 🧠 Brain Dump Mode

Continuous thought capture

```bash
notes brain-dump --tag daily-thoughts
```

Perfect for:

* journaling
* idea capture
* thinking sessions

---

# ⚡ Installation

Ensure you have Python 3 installed. Clone this repository and install the dependencies:

```bash
git clone https://github.com/Aarpit9106/Notes-CLI-Tool.git
cd Notes-CLI-Tool

# Install the package globally
pip install -e .
```

Now the `notes` command is available globally.

---

# 🚀 Usage

## Basic Commands

Add note

```bash
notes add "Buy milk" --tag groceries --mood focused
```

List notes

```bash
notes list
```

View note

```bash
notes view 1
```

Edit note

```bash
notes edit 1 --tag shopping
```

Delete note

```bash
notes delete 1
```

---

# 🔎 Organization Commands

Search notes

```bash
notes search "milk"
```

Filter by mood

```bash
notes mood focused
```

Brain dump

```bash
notes brain-dump --tag thoughts
```

Link notes

```bash
notes link 1 2
```

View links

```bash
notes links 1
```

---

# 📈 Advanced Features

Insights

```bash
notes insights
```

Dashboard

```bash
notes dashboard
```

Memory replay

```bash
notes replay week
```

Send to future

```bash
notes send-future "Review annual goals" --date 2026-12-31
```

---

# 📊 Example Output

```
Daily Dashboard
╭───── Notes Today ─────╮ ╭────── Moods Today ──────╮ ╭── Top Tags Today ──╮
│                       │ │ creative: 1             │ │ ideas: 2           │
│     3                 │ ╰─────────────────────────╯ ╰────────────────────╯
│                       │
╰───────────────────────╯
```

---

# 🏗️ Project Structure

```
Notes-CLI-Tool
│
├── notes/
├── database/
├── commands/
├── utils/
├── main.py
├── setup.py
└── README.md
```

---

# 🎯 Use Cases

* Personal knowledge management
* Second brain system
* Daily journaling
* Developer scratchpad
* Idea capture
* Productivity tracking
* CLI lovers
* Minimalists

---

# 🗺️ Roadmap

* [ ] Export notes to markdown
* [ ] Cloud sync
* [ ] AI summarization
* [ ] Web UI
* [ ] Mobile companion
* [ ] Plugin system

---

# 👨‍💻 Author

Built by **Aarpit Jethwa**
GitHub: https://github.com/Aarpit9106

---

# ⭐ Support

If you like this project:

* Star the repo
* Share with developers
* Contribute features

---

# 🧠 Why this is different

Unlike traditional note apps, this is:

* keyboard-first
* zero distraction
* terminal-native
* knowledge graph enabled
* future messaging
* mood tracking
* analytics built-in

Your **Second Brain inside terminal**
