import json


tasks = []

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def show_tasks():
    if tasks:
        #Sort based on 'done'
        sorted_tasks = sorted(tasks, key=lambda x: x['done'])

        print("\nYour Tasks: ")
        for index, task in enumerate(sorted_tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"- {index}. {task['name']} - {status}")
    else:
        print("No tasks.")

def add_new_task():
    while True:
        task_name = input("Add new Task (or type 'done' to finish)\n")
        if task_name.lower() == 'done':
            break
        tasks.append({'name': task_name, 'done': False})
        save_tasks()
        print(f"Task '{task_name}' has been added")


def mark_task_done():
    if tasks:
        # Display the tasks with "Not Done" tasks first
        sorted_tasks = sorted(tasks, key=lambda x: x['done'])
        print("\nYour Tasks:")
        for index, task in enumerate(sorted_tasks, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index}. {task['name']} - {status}")

        try:
            task_number = int(input("Enter the number of the task you want to mark as done: "))
            if 1 <= task_number <= len(sorted_tasks):
                # Find the task in the original list using the sorted index
                original_index = tasks.index(sorted_tasks[task_number - 1])
                tasks[original_index]['done'] = True
                save_tasks()
                print(f"Task '{tasks[original_index]['name']}' has been marked as Done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to mark as done.")


def remove_task():
    if tasks:
        sorted_tasks = sorted(tasks, key=lambda x: x['done'])
        # Display the tasks with "Not Done" tasks first

        print("\nYour Tasks:")
        for index, task in enumerate(sorted_tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"- {index}. {task['name']} - {status}")


        try:
            task_number = int(input("Enter number of task you want to remove\n"))
            if 1 <= task_number <= len(tasks):
                #FInd the task in the og list using sorted index
                original_index = tasks.index(sorted_tasks[task_number - 1])
                removed_task = tasks.pop(original_index)
                save_tasks()
                print(f"Task '{removed_task['name']}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter Valid Number")
    else:
        print("No task to remove")

#Main
tasks = load_tasks()

while True:
    print("\nWelcome User!\nWhat do you want to do today?\n\n1 - Add Task\n2 - Mark Task as Done\n3 - Remove Task\n4 - Show Tasks\n5 - Exit")

    selection = input("\nChoose option: \n")

    if selection == '1':
        add_new_task()
    elif selection == '2':
        mark_task_done()
    elif selection == '3':
        remove_task()
    elif selection == '4':
        show_tasks()
    elif selection == '5':
        print("Bye!")
        break
    else:
        print("Invalid selection, choose one of the options")