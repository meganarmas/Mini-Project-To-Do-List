to_do_tasks =['Walk the dog', 'Laundry', 'Go on a run', 'Clean kitchen']
print(f"\033[37m{to_do_tasks} \033[31m is not completed.")
print(f"\033[37m {to_do_tasks} \033[0;	32;40m is completed!")

print(f"\033[0;37;40m {to_do_tasks} Testing")

if new_to_do is not current_tasks:
        current_tasks.append({ new_to_do + 'Incomplete'})
        print(f"{new_to_do} has been added to the to-do list!")
    else:
        print(f"{new_to_do} is already in the to-do list.")