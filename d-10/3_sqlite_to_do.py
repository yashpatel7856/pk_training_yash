# end 5:50
import time,sqlite3
  
def startTodoFucntion():
    con = configureConnection() ## database connection object 
    cursor = con.cursor()
 
    uid=int(input("enter id/phnumber"))
    userName=input("enter first user's user name : ")
    if(userName!=""):
        try:
            cursor.execute("Insert into user (id,name) VALUES (?,?)",(uid,userName))
            con.commit()
        except sqlite3.IntegrityError:
            print("couldn't add same name again")
            return 0
    else:
        users=cursor.execute("select * from user where id=(?)",(uid,))
        con.commit
        for user in  users:
            userName=user[1]
        if userName=="":
            print("No user found")
            return 0

    while True:
        option=int(input(f"Active User = {userName}\nselect One option\n1) Add New Task\n2) List Task\n3) Mark Task As Completed\n4) DeleteTask\n5) Exit To-do List\n"))
        if option==1:
            taskNumber=int(input("Enter Task Number : "))
            taskDescription=input("enter Task Description :\n")
            try :
                cursor.execute("insert into task (number,description,status,createdAt,uid) values (?,?,?,?,?)",(taskNumber,taskDescription,0,time.time(),uid))
                con.commit()
            except  sqlite3.IntegrityError:
                print("enter new task number")
                return
            except:
                print("something went wrong while adding task")
                return

        elif option==2:
            try:
                taskData=cursor.execute("select * from task where uid=(?)",(uid,))
                con.commit()
                for task in taskData:
                    print(f'Task Number     :  {task[0]}\nTask desciprion : {task[2]}\nTask status     : {task[3]}\n    date        : {time.asctime(time.localtime(task[4]))}')
            except:
                print("error while listing task")
                return
        elif option==3:
            try:
                taskNumber=int(input("enter task number to mark as completed"))
                cursor.execute("update task set status=1 where number=? and uid=?",(taskNumber,uid))
                con.commit
            except:
                print("error while updating the task status")
                return
        elif option==4:
            taskNumber=int(input("\nEnter task number to Delete : "))
            try:
                cursor.execute("delete from task where number=? and uid=?",(taskNumber,uid))
                con.commit()
            except:
                print("error during deleting task")
                return
        elif option==5:
                print("Closing To-do List\nThank You!!!")
                break

def configureConnection():
    con=sqlite3.connect("todo_sql.db")
    cursor=con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "USER" (
                                id INTEGER PRIMARY KEY,
                                name VARCHAR(10) UNIQUE
                            );
                        ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS TASK (
                                number INTEGER PRIMARY KEY,
                                uid INTEGER,
                                description VARCHAR(40),
                                status BOOLEAN,
                                createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY (uid) REFERENCES "USER" (id)
                            );
                        ''')
    return con

startTodoFucntion()