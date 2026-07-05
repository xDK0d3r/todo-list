# This file handles Task Operations.

task_list = []

# Add Task
def add_task() :
    print("Add Task")
    adding_task = input("Enter Task :")
    task_list.append(adding_task)
    print("task Added Sucessfully")

# View Tasks
def view_tasks() :
    print ("View All Tasks")
    print(task_list)
    

