# This file handles the Main Menu and User input.

print("Welcome to the TO-DO List (CLI)")

# Menu Options
print("1.Add Task")
print("2.Edit Task")
print("3.Delete Task")
print("4.Show All Tasks")
print("5.Exit")

while True :
  
  # User Input
  user_choice = int(input("Please Choose the Option : "))

  # Control flow
  match user_choice :
    case 1 : 
        add_task()
    case 2 :
        edit_task()
    case 3 :
        delete_task()
    case 4 :
        all_task()
    case 5 :
        exit()
    case _ :
        print("Invalid Option!")