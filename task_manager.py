# This file handles Task Operations.

task_list = []

# Add Task
def add_task() :
    # Task add flow
    print("Add Task")
    task_add = input("Enter Task :")
    add_dict = {"task":task_add,
                "completed":False}
    task_list.append(add_dict)
    print("Task Added Sucessfully")

# Edit Task
def edit_task() :
    print("Edit Task")
    task_id = int(input("Select Task by ID :"))
    if 0 <= task_id < len(task_list) :
        task_edit = input("Enter Task :")
        task_list[task_id]["task"] = task_edit
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
    
# Mark Task Completed
def mark_task() :
    print("Mark Task as Completed")
    task_id = int(input("Select Task by ID :"))
    if 0 <= task_id < len(task_list) :
        task_list[task_id]["completed"] = True
    else :
        print("invalid Task ID")

# View Tasks
def view_tasks() :
    print ("View All Tasks")
    print("ID | TASKS")
    # Enumerate
    for index, tasks in enumerate(task_list) :
        print(index," | ",tasks)

# View Completed Tasks
def view_completed_tasks() :
    print("View Completed Tasks")
    print("ID | TASKS")
    # filtering
    for index, tasks in enumerate(task_list) :
        if tasks["completed"] == True :
            print(index," | ",tasks)

# View Pending Tasks
def view_pending_tasks() :
    print("View Pending Tasks")
    print("ID | TASKS")
    #filtering 
    for index, tasks in enumerate(task_list) :
        if tasks["completed"] == False :
            print(index," | ",tasks)
