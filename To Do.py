current_tasks = ['\033[37m walk the dog ' '\033[31m Incomplete', 
            '\033[37m laundry ' '\033[31m Incomplete',
            '\033[37m go on a run ' '\033[32m Complete',
            '\033[37m clean kitchen ' "\033[31m Incomplete"]

def add_task(title="Incomplete"):
    if title is not current_tasks:
        current_tasks.append(title + ' Incomplete')
        print(f"\033[37m {title} has been added to the to-do list")
    else:
        print(f"\033[37m {title} is already in the to-do list.")

def complete_task(mark_complete):
    mark_complete = []
    try:
        index = int(mark_complete) - 1
        if 0 <= index < len(current_tasks):
            current_tasks.replace('\033[31m Incomplete', '\033[32m Complete')
            print(f"Your task has been marked as completed. Great job!")
        else:
            ("Invalid.")
    except TypeError:
        print("This task has not been added! Please add it first.")

def remove_task(delete_task):
    try:
        index = int(delete_task) - 1
        if 0 <= index < len(current_tasks):
            del current_tasks[index]
            print(f"Your task deleted successfully.")
        else:
            print("Invalid task number. Please enter a correct number.")
    except TypeError:
        print("This task has not been added! Please add it first")

def to_do_list():
        while True:
            print("\033[37mWould you like to add tasks, view the current to do list, or remove a take?")
            print("1. Add A Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Quit")
            choice = input("Enter choice: ")
    
            if choice == '1':
                title = input("Enter task to add to do list: ")
                add_task(title)
            elif choice == '2':
                for to_do_task in current_tasks:
                    print(to_do_task)
            elif choice == '3':
                print("What would you mark off as completed? Please enter a number: ")
                complete_task()
            elif choice == '4':
                delete_task = input("Which assignment would you like to mark off? Please enter a number: ")
                remove_task(delete_task)
            elif choice == '5':
                print("Thanks for using the application! Closing To Do List now!")
                break
            else:
                print("Invalid choice. Please select a number from 1 - 5. ")


to_do_list()