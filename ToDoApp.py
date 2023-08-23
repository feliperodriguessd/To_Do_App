"""Create an App to keep track of tasks
- Create a loop
    - Display existing tasks
    - Display an option to add new tasks
    - Option to exit

    Implement Functions and Classes
"""
class TodoApp:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print("Task added:", new_task)

    def delete_task(self):
        self.display_tasks()
        delete_input = input("Type the number of the task you want to delete or 'E' to exit: ")
        if delete_input.lower() == "e":
            return
        if delete_input.isdigit():
            delete_index = int(delete_input) - 1
            if 0 <= delete_index < len(self.tasks):
                deleted_task = self.tasks.pop(delete_index)
                print("Task deleted:", deleted_task)
            else:
                print("Invalid index.")
        else:
            print("Invalid input.")

    def run(self):
        while True:
            user_input = input("Press 'T' to add a new task. Press 'E' to exit. Press 'D' to delete a task: ")
            
            if user_input.lower() == "t":
                new_input = input("Type your new task: ")
                self.add_task(new_input)
            
            elif user_input.lower() == "d":
                self.delete_task()
            
            elif user_input.lower() == "e":
                print("Exiting the app.")
                break
            
            else:
                print("Invalid input. Please enter 'T', 'D', or 'E'.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
