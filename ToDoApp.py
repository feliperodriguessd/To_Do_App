"""Create an App to keep track of tasks
- Create a loop
    - Display existing tasks
    - Display an option to add new tasks
    - Option to exit
"""
tasks = {}

while True:
    print(tasks)
    user_input = input("Press 'T' to add a new task. Press 'D' to delete a task. Press 'E' to exit")

    if user_input == "T" or user_input == "t":
        new_input = input("Type your new task: ")
        tasks.append(new_input)
    elif user_input == "N" or user_input == "n":
        print(tasks)
        break
    else:
        print("Invalid input. Please enter Y or N.")