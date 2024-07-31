import re

to_do_list = []

def add_task():
    title_of_todo = input("Enter task to add to do list: ")
    to_do_list.append({'task': title_of_todo, 'status': 'incomplete'})
    print(f"{title_of_todo} has been added to the to-do list")

def complete_task():
    mark_task = input("Enter the task number to mark as completed.")
    try:
        index = int(mark_task) - 1
        if 0 <= index < len(to_do_list):
            to_do_list[index]['status'] = 'complete'
            print("Task marked as complete.")
        else:
            print("This task has not been added or has already been marked as complete. Please try again!")
    except ValueError:
        print("Value error. Please enter a different number.")

def remove_task():
    delete_task = input("Enter the task number to delete: ")
    try:
        index = int(delete_task) - 1
        if 0 <= index < len(to_do_list):
            del to_do_list[index]
            print(f"Your task deleted successfully.")
        else:
            print("This task has not been added! Please add it first.")
    except ValueError:
        print("Invalid number. Try again!")

def main():
        while True:
            print("Welcome to the To-Do List App. \nMenu")
            print("1. Add A Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Quit")
            choice = input("Enter choice: ")
    
            if choice == '1':
                add_task()
            elif choice == '2':
                for to_do_task in to_do_list:
                    print(to_do_task)
            elif choice == '3':
                complete_task()
            elif choice == '4':
                remove_task()
            elif choice == '5':
                print("Thanks for using the application! Closing To Do List now!")
                break
            else:
                print("Invalid choice. Please select a number from 1 - 5. ")

if __name__ == "__main__":
    main()