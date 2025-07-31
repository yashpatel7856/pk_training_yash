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
    try:
        with open(defaultFileName,"r") as file:
            userData=json.load(file)
    except:
        userData={
        }

    userName=input("enter first user's user name : ")
    if userName not in userData:
        userData[userName]=[]
        userData[userName+".TaskNumberList"]=[]
    u1=User(userName)
    user=u1

    while True:
        option=int(input(f"Active User = {user.name}\nselect One option\n1) Add New Task\n2) List Task\n3) Mark Task As Completed\n4) DeleteTask\n5) Exit To-do List\n"))
        if option==1:
            taskNumber=int(input("Enter Task Number : "))
            while len(userData[userName+".TaskNumberList"])!=0 and taskNumber in userData[userName+".TaskNumberList"]:
                taskNumber=int(input("Same Number TAsk already Exists Please Enter Unique Task Number : "))
            taskDescription=input("enter Task Description :\n")
            t1=Task(taskNumber,taskDescription)
            userData[userName].append(t1.__dict__)
            userData[userName+".TaskNumberList"].append(taskNumber)
        elif option==2:
            userTask=userData[userName]
            if len(userTask)==0:
                print("No Task Added yet !!!\n\n")
                continue
            for task in userTask:
                if task["status"]==1:
                    status="Done"
                else:
                    status="Not Done"
                print(f"Task Number : {task['number']}\nTask Description : {task['description']}\nTask Status : {status}\nCreated At : {time.asctime(time.localtime(task['createdAt']))}\n")
        elif option==3:
            taskNumber=int(input("\nEnter task number to update : "))
            
            if taskNumber not in userData[userName+".TaskNumberList"]:
                print("Task with Given Number Does not Exists !!!")
                continue
            else:
                for task in userData[userName]:
                    if task["number"]==taskNumber:
                        task["status"]=1
        elif option==4:
            taskNumber=int(input("\nEnter task number to Delete : "))
            deleteIndex=None
            if taskNumber not in userData[userName+".TaskNumberList"]:
                print("Task with Given Number Does not Exists !!!")
                continue
            else:
                for index,task in enumerate(userData[userName]):
                    if task["number"]==taskNumber:
                        deleteIndex=index
                del userData[userName][deleteIndex]
                userData[userName+".TaskNumberList"].remove(taskNumber)
        elif option==5:
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


startTodoFucntion()