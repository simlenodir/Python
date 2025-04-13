# Starting with Bismilah
# Creating Task Class
class Task:
    # Initializing
    def  __init__(self, task_name, description, due_date, status=False):
        self.task_name = task_name
        self.description = description
        self.due_date =due_date
        self.status = status

    def __str__(self):
        status_str = 'Completed' if self.status else 'Incomplete'
        return f"Task: {self.task_name} | Description: {self.description} | Due: {self.due_date} | Status: {status_str}"
        
# Creating Todo List
class TodoList:
    def __init__(self):
        self.todo_list = []

    # Adding task to list
    def add_task(self, task_name, description, due_date, status=False):
        # Checking if list is empty
        if len(self.todo_list) == 0:
            try:
                new_task = Task(task_name, description, due_date, status)
                if new_task:
                    self.todo_list.append(new_task)
                    print(f'Your first {task_name} added succesfully')
                else:
                    print('Something is wrong newTask')
            except:
                print("Please Check Input Values")
        else:
            try:
                new_task = Task(task_name, description, due_date, status)
                if new_task:
                    self.todo_list.append(new_task)
                    print(f'Your {task_name} added succesfully')
                else:
                    print('Something is wrong newTask')
            except:
                print("Please Check Input Values")
            

    # Complete Task
    def complete_task(self, task_name):

        print(f'{task_name}')
        # Checking list is empty
        if len(self.todo_list) == 0:
            print(f'Todo list is empty. Would you like add task ?')
            choice = input('Enter your choice  yes/ no: ')
            if choice.lower() == 'yes':
                task_name = input("Enter your task name: ")
                description = input("Enter your task description: ")
                due_date = input("Enter your task due date: ")
                todoList.add_task(task_name, description, due_date)

        # try:
            # find on object from todo_list
            find_task = next((todo for todo in self.todo_list if todo.task_name == task_name), None)
            if find_task: 
                find_task.status = True
                print(f'{find_task} Congrutulations is completed')
            else: 
                print(f"{task_name} is incorrect please check it")
                print(f'{task_name} not found. Would you like add task ?')
                choice = input('Enter your choice  yes/ no: ')
                if choice.lower() == 'yes':
                    task_name = input("Enter your task name: ")
                    description = input("Enter your task description: ")
                    due_date = input("Enter your task due date: ")
                    todoList.add_task(task_name, description, due_date)
        # except:


    def all_tasks(self):
        if len(self.todo_list) == 0:
            print('Sorry task list is empty')
        else:
            for todo in self.todo_list:
                print(f'These all list: {todo}')

    def incompleted_tasks(self):
        if len(self.todo_list) == 0:
              print('Sorry task list is empty')
        else:
            for todo in self.todo_list:
                if todo.status == False:
                    print(f'These all Incomplete list: {todo}')

# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.

todoList = TodoList()

def print_menu():
    
    print("\nTodo List Management Menu:")
    print("1. Add  a task")
    print("2. Complete task")
    print("3. All Todo list")
    print("4. Only incomplete tasks")
    print("5. Exit")

    choice = input("Enter your choice 1-5: ")

    if choice == '1':
        task_name = input("Enter your task name: ")
        description = input("Enter your task description: ")
        due_date = input("Enter your task due date: ")
        todoList.add_task(task_name, description, due_date)
    elif choice == '2':
        task_name = input("Enter your task name: ")
        todoList.complete_task(task_name)
    elif choice == '3':
        todoList.all_tasks()
    elif choice == '4':
        todoList.incompleted_tasks()

while True:
    print_menu()

    # break