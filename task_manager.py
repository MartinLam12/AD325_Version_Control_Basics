class TaskManager:
    def __init__(self):
        self.task_file = 'tasks.txt'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.task_file, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index} - {task}")

    def delete_task(self, index):
        if self.tasks:
            self.tasks.pop(index) # Adjusted to correctly delete the task at the given index
            self.save_tasks()
        
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = f"{self.tasks[index]} (completed)"
            self.save_tasks()        
        else:
            print("No tasks to complete.")

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_description
            self.save_tasks()
            print(f"Task {index + 1} updated successfully.")
        else:
            print("Error: Task index out of range.")

