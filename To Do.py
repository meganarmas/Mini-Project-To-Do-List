to_do_tasks =['Walk the dog', 'Laundry', 'Go on a run', 'Clean kitchen']

def to_do_list():
    while True:
        print("Would you like to view list, add items, or removed items?")
        print("1. Add A Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter choice: ")
    
        if choice == '1':
            print("Add A Task")
            new_to_do = input("Enter what to add to the to-do list for today?: ")
            if new_to_do is not to_do_list:
                to_do_tasks.append(new_to_do)
                print(f"{new_to_do} has been added to the to-do list!")
            else:
                print(f"{new_to_do} is already in the to-do list.")
        elif choice == '2':
            for to_do_task in to_do_tasks:
                print(to_do_task)
        elif choice == '3':
            mark_complete = input("Which task was completed?: ")
            if mark_complete in to_do_task:
                pass
        elif choice == '4':
            remove_item = input("Enter what to remove from the to-do list?: ")
            if remove_item in to_do_tasks:
               to_do_tasks.remove(remove_item)
               print(f"{remove_item} has been removed to the shopping list!")
        elif choice == '5':
            print("Thanks for using the application! Closing To Do List now!")
            break
        else:
            print("Invalid choice. Please use a number from 1 - 5. ")
            

to_do_list()