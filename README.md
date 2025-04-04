# daily-planner-cli


A minimalist command-line planner tool built in Python. Designed for focused individuals who want to log daily tasks, track completions, and stay organized. Inspired by the mindset of *The Bearded Planner* — automate the chaos, plan with purpose.

---

## 🚀 Features
- Add tasks to your daily list
- View today's task list
- Mark tasks as done
- Clear all tasks
- Simple local storage using JSON

---

## 🛠️ Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/daily-planner-cli.git
cd daily-planner-cli
```
2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Run the script directly:
```bash
python planner.py [command]
```

---

## 📖 Usage
### Add a Task
```bash
python planner.py add "Go to the gym"
```
### List Today's Tasks
```bash
python planner.py list
```
### Mark a Task as Done
```bash
python planner.py done 2
```
### Clear All Tasks
```bash
python planner.py clear
```

---

## 📁 File Structure
```
.
├── planner.py       # Main CLI script
└── tasks.json       # Auto-generated storage file
```

---

## 🧠 Philosophy
This tool is intentionally simple. It’s for those who believe in:
- Planning one day at a time
- Clean interfaces, low friction
- Getting things done with intention

> "Plan it. Build it. Automate the rest." – The Bearded Planner

---

## 📬 Contribute
Have a feature idea or want to collaborate? Submit an issue or a PR!

---

## 📜 License
MIT License
