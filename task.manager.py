#=====importing libraries===========
import datetime
from datetime import date, datetime

 
#below code asks for a username and password, and if the username is not already in the list, and the
    #password is confirmed, it writes the username and password to a file
def reg_user ():
    global username_list 
    while True:
        with open('user.txt', 'a+') as file:
            new_username = input("user name :")
            new_userpassword = input("enter password:")
            password_confirmation = input("please confirm password:")

            if new_username in username_list :
                print("username exists")
                
            elif new_userpassword == password_confirmation :
                print("you have registered sucessfully")
                file.write(f"\n{new_username}, {new_userpassword}")
                break

            else:
                print("only admin is allowed to register a user")

# The below code is creating a function called add_task. The function is opening a file called
# tasks.txt and appending the file. The function is asking the user to input the following details:
# task_user_name, task_title, task_description, task_duedate, current_date, task_complete. The
# function is writing the user input to the file.
def add_task():
        with open("tasks.txt", "a+") as file:
            print(" fullin the following details")
            task_user_name =input("enter the person who the task assigned to:")
            task_title = input("name of the task:")
            task_description = input("what is the task :")
            task_duedate = input("enter due date of task:")
            current_date = input("enter current date:")
            task_complete = "No"
            file.write(f"\n{task_user_name}, {task_title}, {task_description}, {task_duedate}, {current_date}, {task_complete}")

#It opens the file, reads the file, splits the data, and prints the data
def view_all():    
        with open("tasks.txt", "r+") as file :
            for line in file:
                split_data = line.split(", ")
                peoples_names = f"""name:{split_data[0]}\ntask:{split_data[1]}\ntask descriiption:{split_data[2]}\ndue date:{split_data[3]}
                            \ncurrent date: {split_data[4]}\n is the task complete: {split_data[5]}"""
                print(peoples_names)

    #It reads a file, creates a dictionary, prints the dictionary, and then asks the user to select a
    #task.
def view_mine():
    tn= 1
    dic_task = {}
    with open ("tasks.txt", "r+") as file:
        for line in file :
            dic_task[tn] = line.split(", ")
            task_username, task_title, task_description, task_duedate, current_date, task_complete = line.split(", ")
            if username == task_username:
                print(f"tn:{tn}\nName:{task_username}\n{task_title}\ntask_description:{task_description}\ntask due date: {task_duedate} \n current date:{current_date}\n task complete:{task_complete}")
            tn +=1
        task_choice = int(input("select a task by entering a number or input '-1' for main menu:"))

        if task_choice == -1:
            print("going home")  
        
        else:

            task_edit_options = input("\nSelect 'TE' to edit \nMC to mark as complete: \n").lower()
          
          # Replacing the last item in the list with the word "yes"
            chosen_task = dic_task[task_choice]

            if task_edit_options == "mc":

                print(chosen_task)
                task_complition_answer = chosen_task[-1]

                if task_complition_answer == "No\n":
                    chosen_task[-1] = chosen_task[-1].replace("No", "yes")
                print(chosen_task)

          # The above code is asking the user to input a new due date for the task.

            if task_edit_options == "te":
                    new_usertask_edit_options = input("cd - change due date \ncu - change user name").lower()
                    if new_usertask_edit_options == "cd":
                        print(f"The current due date of the task is {chosen_task[3]}")
                        new_usertask_date_edit = input("enter the new date :\n")
                        chosen_task[3] = chosen_task[3].replace(chosen_task[3], new_usertask_date_edit)
                        print(f"the new due date is {new_usertask_date_edit}")

                    # The above code is replacing the current user name with the new user name.
                    elif new_usertask_edit_options == "cu":
                        print(f"The current user is {chosen_task[0]}\n")
                        new_user_name = input("enter new user name for task: \n")
                        print(new_user_name)
                        chosen_task[0] = chosen_task[0].replace(chosen_task[0], new_user_name)
                        print(f"the new user name for task is {new_user_name}")
                        
                    else:
                        pass
                       
                       # Writing the values of the dictionary to a file.      
            with open ("tasks.txt","w+") as file:
                for line in dic_task.values():
                    file.write(", ".join(line))


    
    #It counts the number of lines in the tasks.txt and user.txt files and prints the results.
    
def display_stats():
    task_num = 0
    user_num = 0
    with open ("tasks.txt", "r") as task_title :
        for line in task_title :
            task_num += 1
    print(f"\ntotal number of tasks are: {task_num}")

    with open("user.txt", "r") as username :
        for line in username :
            user_num += 1
    print(f"total number of user are {user_num}\n")

    # This function generates a report of the tasks in the task list
    # It reads the tasks.txt file and generates a report of the number of tasks, the number of tasks
    # completed, the number of tasks incomplete, the number of overdue tasks, and the percentage of
    # incomplete tasks. 
    
    # It also reads the user.txt file and generates a report of the number of users, the number of tasks
    # assigned to each user, the percentage of tasks assigned to each user, the number of tasks completed
    # by each user, the percentage of tasks completed by each user, the number of tasks incomplete for
    # each user, the percentage of tasks incomplete for each user, and the percentage of overdue tasks for
    # each user. 
    # The reports are written to the tasks_overview.txt and user_overview.txt files. 
    # The function returns the user report.
    
def generate_reports():   
    with open ("tasks_overview.txt", "w") as task_track:
        task_num = 0
        task_complete = 0
        task_incomplete = 0 
        overdue_task = 0
        # current_date = datetime.today()
        with open ("tasks.txt", "r") as task_title :
            for line in task_title :
                task_num += 1
                line = line.split(", ")
                if line [-1].strip("\n") == "yes":
                    task_complete +=1
                elif line[-1].strip("\n") == "No":
                    task_incomplete += 1
                    overdue_task += 1
                #today = date.today()
                # new_given_date = today.strftime("%d %b %Y")
                percentage_incomplete = (task_incomplete/(task_complete + task_incomplete))*100

            print(f"""total number of task: {task_num}\n)
            the number of task complete: {task_complete}\n         
            the number of incomplete task :{task_incomplete}\n 
            the over due task : {overdue_task}\n  
            incomplete task precentage : {percentage_incomplete}%""")
            
            task_track.write(f"""total number of task : {task_num}
            total number of task complete: {task_complete}
            total number of incomplete task : {task_incomplete}
            total of over due task : {overdue_task}
            precentage of incomplete task : {percentage_incomplete}%""")

    with open("user_overview.txt","w") as user_track:
        with open ("user.txt", "r") as username:
            username_content = username.readlines()
            output = f"total number of user {len(username_content)}\n"
            with open ("tasks.txt","r") as tasks_file:
                tasks_list = tasks_file.readlines()

                for line in username_content : #r =admin

                    line = line.replace("\n", "").split(", ")
                    user = line[0]
                    print(user)

                    # current_date = datetime.today()

                    user_task_count = 0
                    percentage_task_complete = 0
                    percentage_task_incomplete = 0
                    task_complete = 0
                    task_incomplete = 0
                    percentage_overdue = 0


                    for task in tasks_list:
                        task = task.split(", ")
                        task_user = task[0]

                        if user == task_user:
                           user_task_count +=1
                           print(f"WE ARE HERE NOW {user_task_count}")

                        elif task[-1].strip("\n").lower() == "yes":
                            task_complete += 1
                        else:
                            task_incomplete += 1

                    task_assigned_percentage = user_task_count/len(tasks_list)*100
                    try:
                        percentage_task_complete = (task_complete / user_task_count)*100
                        percentage_task_incomplete = (task_incomplete / user_task_count)*100
                        percentage_overdue = (task_incomplete / user_task_count) *100
                    except ZeroDivisionError:
                        percentage_task_incomplete = 0    
                        percentage_task_complete = 0
                        percentage_overdue = 0
                        
                    
                    output += f"""{user}\n\ttotal task is :{user_task_count} 
                    the total percentage assigned to {user} :{round(task_assigned_percentage, 2 )}%
                    the total number of completed task are :{task_complete}
                    the percentage of task that are completed :{percentage_task_complete}%
                    the percentage of task that are incomplete:{percentage_task_incomplete}%
                    thepercentage of the that are overdue :{percentage_overdue}%
                    \n"""
            print(output)
            user_track.write(output)
        return output
# The below code is asking the user to enter a username and password. If the username and password are
# correct, the user will be logged in. If the username and password are incorrect, the user will be
# asked to enter a username and password again.

with open("user.txt", "r") as file:
    username_password = file.readlines()
    username_list = []
    while True :
        logged_in = False
        print("please enter following details :")
        username = input("please enter user name:\n")
        password = input("please enter password:\n")
        for i in username_password :
            split_data = i.strip().split(", ")
            cor_user = split_data[0].strip("\n")
            username_list.append(cor_user)
            cor_pass = split_data[1].strip("\n")
            if password == cor_pass and username == cor_user :
                logged_in = True
                break
            elif password != cor_pass and cor_user != username:
                continue
            else:
                print("user name does not exist, enter a username and password")
        if logged_in :
            print("logged in ")
            break
# The below code is asking the user to enter a new username and password.

while True:
    if username == "admin":

            menu = input("""r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            te - task edit
            e  - Exit
            ds - display stats
            gr - generate reports
            :""").lower()
    else: 
        menu = input("""
                 va - View all tasks
                 vm - view my task
                 e - Exit
                 te - task edit
                 ds - display stats
                 :""").lower()
# This is the code that is asking the user to enter a new username and password.
        
    if menu == "r" and username == "admin":
        reg_user()
    elif menu == "r" and username != "admin":
        print("Only Admin is allowed to register! ")
    elif menu == "te":
        print("task edit")
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()    
    elif menu == "ds" and username == "admin":
        display_stats()
    elif menu == "gr":
        generate_reports()
    elif menu == "e":
        print("goodby !!!")
        exit()

    else :
        print(" you have made the wrong choice, please try again")