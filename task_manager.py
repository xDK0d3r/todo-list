# This file handles Task Operations.

task_list = []

# Add Task
def add_task() :
    # Task add flow
    print("Add Task")
    task_add = input("Enter Task :")
    task_list.append(task_add)
    print("Task Added Sucessfully")

# Edit Task
def edit_task() :
    print("Edit Task")
    task_id = int(input("Select Task by ID :"))
    if 0 <= task_id < len(task_list) :
        task_edit = input("Enter Task :")
        task_list[task_id] = task_edit
        print("Task Edited Sucessfully")
    else :
        print("invalid Task ID")

# Delete Task
def delete_task() :
    print("Delete Task")
    task_id = int(input("Select Task by ID :"))
    if 0 <= task_id < len(task_list) :
        task_list.pop(task_id)
    else :
        print("invalid Task ID")
    
# View Tasks
def view_tasks() :
    print ("View All Tasks")
    print("ID | TASKS")
    # Enumerate
    for index, tasks in enumerate(task_list) :
        print(index," | ",tasks)


    
    

