import json
import os
import time

tasks = []
times = []

def load_tasks():
    global tasks
    if os.path.exists("todolist.json"):
        with open("todolist.json", "r") as file:
            tasks = json.load(file)

def save_tasks():
    with open("todolist.json", "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks():
    if not tasks:
        print("There are no tasks to show.")
    else:
        display_tasks = tasks
        if sorted_by_time:
            display_tasks = sorted(tasks, key=lambda t: t["time"])
        for i, task in enumerate(display_tasks):
            print(f"{i}. {task['task']} {task['status']}")

load_tasks()

while True:
    print("==To Do List==")
    print("1. Add task")
    print("2. Done task")
    print("3. Remove task")
    print("4. Change Priority")
    print("5. List all tasks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        appended_time = time.time()
        times.append(appended_time)
        save_tasks()
        print("==To Do List==")
        for task in tasks:
            print(task)

    elif choice == 2:
        while True:
            try:
                print("Enter completed task number:")
                i = int(input())


                print(f"{tasks[i]} completed.")
                tasks[i-1] = tasks[i-1] + "[✓]"
                save_tasks()
                print("==To Do List==")
                for task in tasks:
                    print(task)
                break
            except (IndexError, ValueError):
                print("Invalid task number.")
                save_tasks()


    elif choice == 3:
        while True:
            try:
                print("Enter task you want to remove: ")
                x = int(input())

                removed_task = tasks.pop(x-1)
                save_tasks()
                print("==To Do List==")
                for task in tasks:
                    print(task)
                break
            except (IndexError, ValueError):
                print("Invalid task number.")
                save_tasks()

    elif choice == 4:
        while True:
            try:
                print("Enter current priority:")
                current = int(input())
                print("Enter new priority:")
                priority = int(input())

                task = tasks.pop(current-1)
                tasks.insert(priority, task)

                save_tasks()
                print("==To Do List==")
                for task in tasks:
                    print(task)
                break
            except (IndexError, ValueError):
                print("Invalid task number.")


    elif choice == 5:
        save_tasks()
        print("==To Do List==")
        for task in tasks:
            print(task)

    elif choice == 6:
        save_tasks()
        print("Exit")
        break
    else:
        print("Invalid choice")

