# This file handles storage operations.

# import json module
import json

# import path module
from os import path

# File Loading Flow

# Check for tasks.json
def load_tasks() :
    # Handle Exception
    try :
      if path.exists("tasks.json") :
       tasks_file = open("tasks.json","r")
       tasks = json.load(tasks_file)
       tasks_file.close()
       return tasks
      else :
        tasks = []
        return tasks
    except json.decoder.JSONDecodeError :
       print("File was Corrupted (Json Decode Error)")
       print("Delete the file and try again")
       exit()
    
# File Saving Flow
def save_tasks(tasks) :
    tasks_file = open("tasks.json","w")
    json.dump(tasks,tasks_file)
    tasks_file.close()
    