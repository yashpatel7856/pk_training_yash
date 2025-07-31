# start time : 11:30
# end time : 1:00
import time,json
class User:
    def __init__(self,name):
        self.name=name

class Task:
    def __init__(self,number,description,status=0,createdAt=time.time()):
        self.number=number
        self.description=description
        self.status=status
        self.createdAt=createdAt

    
def startTodoFucntion():
    defaultFileName="todo_data.json"
    taskHistory={
        "u1":[],
        "u2":[],
        "u1TaskNumberList":[],
        "u2TaskNumberList":[]
    }
    userName=input("enter first user's user name : ")
    u1=User(userName)
    userName=input("enter first user's user name : ")  #
    u2=User(userName)
    userOption=int(input("Select The User Number (1/2)\n"))  #
    if userOption==1:
        user=u1
    else:
        user=u2
    
    try:
        with open(defaultFileName,"r") as file:
            userData=json.load(file)
    except:
        userData={
            "u1":[],
            "u2":[],
            "u1TaskNumberList":[],
            "u2TaskNumberList":[]
        }





    while True:
        option=int(input(f"Active User = {user.name}\nselect One option\n1) Add New Task\n2) List Task\n3) Mark Task As Completed\n4) DeleteTask\n5) Exit To-do List\n6) User Change\n"))
        if option==1:
            taskNumber=int(input("Enter Task Number : "))
            if user==u1:
                while len(userData["u1TaskNumberList"])!=0 and taskNumber in userData["u1TaskNumberList"]:
                    taskNumber=int(input("Same Number TAsk already Exists Please Enter Unique Task Number : "))
            else:
                while len(userData["u2TaskNumberList"])!=0 and taskNumber in userData["u2TaskNumberList"]:
                    taskNumber=int(input("Same Number TAsk already Exists Please Enter Unique Task Number :  "))
            taskDescription=input("enter Task Description :\n")
            t1=Task(taskNumber,taskDescription)
            if user==u1:
                userData["u1"].append(t1.__dict__)
                userData["u1TaskNumberList"].append(taskNumber)
            else:
                userData["u2"].append(t1.__dict__)
                userData["u2TaskNumberList"].append(taskNumber)
        elif option==2:
            if user==u1:
                userTask=userData["u1"]
            else:
                userTask=userData["u2"]
            for task in userTask:
                if task["status"]==1:
                    status="Done"
                else:
                    status="Not Done"
                print(f"Task Number : {task['number']}\nTask Description : {task['description']}\nTask Status : {status}\nCreated At : {time.asctime(time.localtime(task['createdAt']))}\n")
        elif option==3:
            taskNumber=int(input("\nEnter task number to update : "))
            if user==u1:
                if taskNumber not in userData["u1TaskNumberList"]:
                    print("Task with Given Number Does not Exists !!!")
                    continue
                else:
                    for task in userData["u1"]:
                        if task["number"]==taskNumber:
                            task["status"]=1
            else:
                if taskNumber not in userData["u2TaskNumberList"]:
                    print("Task with Given Number Does not Exists !!!")
                    continue
                else:
                    for task in userData["u2"]:
                        if task["number"]==taskNumber:
                            task["status"]=1
        elif option==4:
            taskNumber=int(input("\nEnter task number to update : "))
            deleteIndex=None
            if user==u1:
                if taskNumber not in userData["u1TaskNumberList"]:
                    print("Task with Given Number Does not Exists !!!")
                    continue
                else:
                    for index,task in enumerate(userData['u1']):
                        if task["number"]==taskNumber:
                            deleteIndex=index
                    del userData["u1"][deleteIndex]
                    userData["u1TaskNumberList"].remove(taskNumber)
            else:
                if taskNumber not in userData["u2TaskNumberList"]:
                    print("Task with Given Number Does not Exists !!!")
                    continue
                else:
                    for index,task in enumerate(userData["u2"]):
                        if task["number"]==taskNumber:
                            deleteIndex=index
                    del userData["u2"][deleteIndex]
                    userData["u2TaskNumberList"].remove(taskNumber)
        elif option==5:
            print(userData)
            try:
                with open(defaultFileName,"a+") as f:
                    f.seek(0)
                    f.truncate()
                    json.dump(userData,f)
                    print("Closing To-do List\nThank You!!!")
                    break
            except:
                print("something went wrong !!!")
                break
        elif option==6:
            userOption=int(input("enter user number 1/2\n"))
            if userOption==1:
                user=u1
            else:
                user=u2

startTodoFucntion()