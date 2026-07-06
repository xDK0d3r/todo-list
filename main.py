# This file handles the Main Menu and User input.

# import tasks
import task_manager

print("Welcome to the TO-DO List (CLI)")

# Menu Options
print("1.Add Task")
print("2.Edit Task")
print("3.Delete Task")
print("4.Show All Tasks")
print("5.Mark Task as Completed")
print("6.Exit")

while True :
  
  # User Input
  user_choice = int(input("Please Choose the Option : "))

  # Control flow
  match user_choice :
    case 1 : 
       task_manager.add_task()
    case 2 :
        task_manager.edit_task()
    case 3 :
        task_manager.delete_task()
    case 4 :
        task_manager.view_tasks()
    case 5 :
        task_manager.mark_task()
    case 6 :
        exit()
    case _ :
        print("Invalid Option!")