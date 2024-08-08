def show_menu():
    print("\n1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit\n")

def view_todo_list(tasks):
    if len(tasks) == 0:
        print("\nYour To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    view_todo_list(tasks)
    if len(tasks) > 0:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Cell 3: Main loop to run the To-Do list program
tasks = []
while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        view_todo_list(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
