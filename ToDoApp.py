"""Create an App to keep track of tasks
- Create a loop
    - Display existing tasks
    - Display an option to add new tasks
    - Option to exit
"""
tasks = []

while True:
    user_input = input("Press 'T' to add a new task. Press 'E' to exit. Press 'D' to delete a task.")

    if user_input.lower() == "t":
        new_input = input("Type your new task: ")
        tasks.append(new_input)
        print("Tasks: ", tasks)
    
    elif user_input.lower() == "d":
        for index, task in enumerate(tasks, start=1):
            print(f"Press {index} to delete '{task}'")

        delete_input = input("Type the number of the task you want to delete or 'E' to exit")
        if delete_input.isdigit():
            delete_index = int(delete_input) - 1
            if 0 <= delete_index < len(tasks):
                del tasks[delete_index]
                print(tasks)
            else:
                print(f"invalid Index, please type a number between 0 and",len(tasks))
        else:
            print(tasks )

    elif user_input.lower() == "e":
        break

    else:
        print("Invalid input. Please enter 'T', 'D' or 'E'")