# This file handles the Main Menu and User input.

# import tasks
import task_manager

print("Welcome to the TO-DO List (CLI)")

def menu() :
   # Menu Options
      print("Menu")
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
  print("press 0 for view the Menu or Press 8 for Exit the Program")
  
  # Handle Exception
  try :
    user_choice = int(input("Please Choose the Option : "))
  except ValueError :
     print("Invalid Menu Option")
     continue

  # Control flow
  match user_choice :
    case 0 :
      menu()
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
        task_manager.view_completed_tasks()
    case 7 :
        task_manager.view_pending_tasks()
    case 8 :
          print("Exit form To-Do List (cli)")
          break
    case _ :
        print("Invalid Option!")