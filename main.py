# This file handles the Main Menu and User input.

# import tasks
import task_manager

print("Welcome to the TO-DO List (CLI)")

def menu() :
  # Menu Options
  print("1.Add Task")
  print("2.Edit Task")
  print("3.Delete Task")
  print("4.Show All Tasks")
  print("5.Mark Task as Completed")
  print("6.View Completed Tasks")
  print("7.View Pending Tasks")
  print("8.Exit")

menu()

while True :
  
  # User Input
  user_choice = int(input("Please Choose the Option : "))

  # Control flow
  match user_choice :
    case 1 :
       menu() 
       task_manager.add_task()
    case 2 :
        menu()
        task_manager.edit_task()
    case 3 :
        menu()
        task_manager.delete_task()
    case 4 :
        menu()
        task_manager.view_tasks()
    case 5 :
        menu()
        task_manager.mark_task()
    case 6 :
        menu()
        task_manager.view_completed_tasks()
    case 7 :
        menu()
        task_manager.view_pending_tasks()
    case 8 :
          print("Exit from To Do List")
          exit()
    case _ :
        print("Invalid Option!")