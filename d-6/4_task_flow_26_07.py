# Problem 2: Resilient Workflow Automation Engine with Retry and Dependency Graph

# Problem Statement

# Build a fault-tolerant workflow automation engine that manages task execution order based on dependencies. The system should:

# Support Task objects with execution time and dependency links.
# Automatically retry failed tasks up to a limit.
# Detect circular dependencies and prevent deadlocks.
# Track execution states (PENDING, RUNNING, COMPLETED, FAILED).
# Execute tasks respecting dependency order.

# Sample Input

# python
# t1 = Task("Download Data", 5)
# t2 = Task("Clean Data", 5, [t1])
# t3 = Task("Train Model", 10, [t2])
# t4 = Task("Evaluate Model", 5, [t3])

# wf = Workflow([t4])
# wf.execute()

#  Sample Output

# Running: Download Data
# Completed: Download Data
# Running: Clean Data
# Failed: Clean Data, Retry 1
# Running: Clean Data
# Completed: Clean Data
# Running: Train Model
# Completed: Train Model
# Running: Evaluate Model
# Completed: Evaluate Model

# start time : 4:20
# end time : 5:51

import random

class Task:
    detectLoop=[] 
    def __init__(self, name, retryCount, dependentOnTask=[]):
        self.name = name
        self.retryCount = retryCount
        self.dependentOnTask = dependentOnTask
        self.executCount = 0
        self.State="PENDING"  #PENDING, RUNNING, COMPLETED, FAILED)
        self.isCompleted = False
        self.isExhausted = False

    def start(self):
        if self in Task.detectLoop:
            print(f"Circular depency detected")
            return
        Task.detectLoop.append(self)
        self.State="RUNNING"
        for task in self.dependentOnTask:
            if not task.isCompleted:
                output = task.start()
                if task.isExhausted:
                    print(f"Execution of task '{self.name}' stopped. Dependent task '{task.name}' exhausted.")
                    self.isExhausted = True
                    return


        # if self.isExhausted:
        #     print(f"Task '{self.name}' is already exhausted. Skipping execution.")
        #     return


        while self.executCount < self.retryCount:
            self.executCount += 1
            print(f'{self.name} task started.')  #  execution count = {self.executCount}, Max retries = {self.retryCount}
            if random.random() > 0.5:
                self.isCompleted = True
                self.State="COMPLETED"
                print(f'{self.name} Task Completed.')
                return
            else:
                self.State="FAILED"
                print(f'{self.name} Failed. Retry {self.executCount}')


        self.isExhausted = True
        print(f'{self.name} max retry count exceeded (count = {self.executCount})')

class WorkFlow:
    def __init__(self, bootUpTask):
        self.bootUpTask = bootUpTask

    def execute(self):
        for task in self.bootUpTask:
            task.start()

t1 = Task("Download Data", 1)
t2 = Task("Clean Data", 3, [t1])
t3 = Task("Train Model", 4, [t2])
t4 = Task("Evaluate Model", 5, [t3])

wf = WorkFlow([t4])
wf.execute()
