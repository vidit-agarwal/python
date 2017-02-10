import sys
task={}
#f = open("task_file.txt", "w+")
while(1) :

  def add() :
        task_name = input("Emter task name :")
        task_des = input ("Enter task description : ")
        task2 = {task_name  : task_des }
        f = open("task_file.txt", "a+")
        task.update(task2)
        """f.write(task_name)
        f.write(":")
        f.write(task_des)
        f.write("\n")"""
        print("THE UPDATED LIST : ")
        display()


  def delete():
       print("Delete Task called")
       usr_input = (input("Enter the name of Task to delete"))
       if usr_input in task.keys() :
          del task[usr_input]
          print("THE UPDATED LIST : ")
          display()
       else  :
           print("No TASK with this name")



  def modify() :
      print("Modify Task called")
      usr_input= input("\n\tEnter the task name to be modified : ")
      if usr_input in task.keys():
          task_name_new = input("Enter new task name")
          task_des_new = input("Enter the new task description")
          #task[usr_input]= task_des_new
          task2 = {task_name_new  : task_des_new }
          task.update(task2)
          del task[usr_input]
          print("THE UPDATED LIST : ")
          display()




  def search() :
      print("Search Task Called")
      usr_input = input("\n\tEnter the Task Name to search : ")
      if usr_input in task.keys() :
           print("\n\tThe Task Name is : ", usr_input)
           print("\n\t The Task Description is : ", task[usr_input])

  def display() :
      for i,j in task.items() :
            print("Task Name  : {0}, \nTask Description : {1}". format(i,j))

  def exit() :
      print("\n\t THE TASK MANAGER IS EXITING : ")
      sys.exit()


  taskaction = {
      "Add Task" : add,
      "Delete Task" : delete,
      "Modify Task" : modify,
      "Search Task" : search,
      "Display Task": display,
      "Exit":exit
   }
  print (
       """\n
      "Add Task   " : add
      "Delete Task" : delete
      "Modify Task" : modify
      "Search Task" : search
      "Display Task": display
      "Exit ":exit

       """
   )

  usr_input = input("\nEnter your choice : ")
  taskaction.get(usr_input)()

