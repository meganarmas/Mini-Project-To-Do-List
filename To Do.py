current_tasks = ['Walk the dog ' '\033[31m Incomplete', 
            "\033[37m Laundry " '\033[31m Incomplete',
            "\033[37m Go on a run " '\033[32m Complete',
            "\033[37m Clean kitchen " "\033[31m Incomplete"]

def add_task(new_to_do="Incomplete"):
    if new_to_do is not current_tasks:
        current_tasks.append({ new_to_do + 'Incomplete'})
        print(f"{new_to_do} has been added to the to-do list!")
    else:
        print(f"{new_to_do} is already in the to-do list.")
    

def remove_task(remove_item):
        if remove_item in current_tasks:
            current_tasks.remove(remove_item)
            print(f"{remove_item} has been removed fom your to do list!")
        else:
            print("Task is not on the list - please add it first.")

def to_do_list():
        while True:
            print("\033[37m Would you like to view list, add items, or removed items?")
            print("1. Add A Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Quit")
            choice = input("Enter choice: ")
    
            if choice == '1':
                user = input("Enter task to add to do list: ")
                add_task()
            elif choice == '2':
                for to_do_task in current_tasks:
                    print(to_do_task)
            elif choice == '3':
                try:
                    mark_complete[] = current_tasks.replace("Incomplete", "Complete")
                    if mark_complete in current_tasks:
                        mark_complete = current_tasks.replace("Incomplete", "\033[32m Complete")
                        print(f"You have completed {mark_complete}! Great job!")
                    else:
                        print("Invalid.")
                except TypeError:
                    print("This task has not been added! Please add it first")
            elif choice == '4':
                remove_item = input("Enter what to remove from the to-do list?: ")
                remove_task()
            elif choice == '5':
                print("Thanks for using the application! Closing To Do List now!")
                break
            else:
                print("Invalid choice. Please select a number from 1 - 5. ")

to_do_list()