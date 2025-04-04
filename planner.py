# daily_planner_cli/planner.py
import json
import os
import argparse
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False, "date": str(datetime.now().date())})
    save_tasks(tasks)
    print("\u2714 Task added!")

def list_tasks():
    tasks = load_tasks()
    today = str(datetime.now().date())
    print("\U0001F4C5  Today's Tasks:")
    for i, t in enumerate(tasks):
        if t["date"] == today:
            status = "[x]" if t["done"] else "[ ]"
            print(f"{status} {i+1}. {t['task']}")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("\u2714 Task marked as done")
    except IndexError:
        print("Invalid task number")

def clear_tasks():
    save_tasks([])
    print("\u274C All tasks cleared")

def main():
    parser = argparse.ArgumentParser(description="The Bearded Planner CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("task", type=str, help="Task description")

    # List tasks
    subparsers.add_parser("list")

    # Mark task done
    parser_done = subparsers.add_parser("done")
    parser_done.add_argument("index", type=int, help="Task number to mark done")

    # Clear all tasks
    subparsers.add_parser("clear")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.index)
    elif args.command == "clear":
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
