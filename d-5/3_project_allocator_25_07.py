# You are building a system to allocate employees to projects based on their "skills", availability, and project "priority". Each employee can work on only one project at a time. Each project requires a specific number of employees with certain "skills", and has a "priority" level. Your goal is to assign employees to the highest "priority" projects first, fulfilling their required skill sets as much as possible.

# The challenge is to maximize the number of fully staffed projects while respecting constraints.

# Rules & Constraints:

# 1. One Project per Employee:
#    Each employee can be assigned to at most one project.

# 2. Project Completion Criteria:
#    A project is considered staffed only if all of the following are met:

#    - The required number of employees is met ("numPeopleRequired")
#    - The required "skills" are covered collectively by the assigned employees

# 3. "priority"-Based Allocation:
#    Projects with lower "priority" numbers are handled first.

# 4. Skill Matching:

#    - Employees may have overlapping "skills".
#    - You must select a combination of "available" employees whose combined skill sets satisfy the "requiredSkills" of the project.


# Example Input:

employees = [
{ "id": "E1", "skills": ["Python", "Django"], "available": True },
{ "id": "E2", "skills": ["React"], "available": True },
{ "id": "E3", "skills": ["Django"], "available": True },
{ "id": "E4", "skills": ["Java", "Spring"], "available": True },
{ "id": "E5", "skills": ["Java"], "available": True },
{ "id": "E6", "skills": ["NodeJS"], "available": True }
]

projects = [
{
"id": "P1",
"requiredSkills": ["Python", "Django"],
"numPeopleRequired": 2,
"priority": 1
},
{
"id": "P2",
"requiredSkills": ["Java", "Spring"],
"numPeopleRequired": 2,
"priority": 2
},
{
"id": "P3",
"requiredSkills": ["React", "NodeJS"],
"numPeopleRequired": 2,
"priority": 3
}
]


# Expected Output:

# {
# projectAssignments: {
# P1: ["E1", "E3"],
# P2: ["E4", "E5"]
# },
# unassignedEmployees: ["E2"],
# unstaffedProjects: ["P3"]
# }

# start time : 4:20
# end time 6:40

def assignProject(employees,projects):
    ""
    projectEmployeeData=doEmployeeAllocation(employees,projects)
    return projectEmployeeData

def doEmployeeAllocation(employees,projects):
    projectAssignedToEmployeeList=[]
    print(employees)
    itemToRemove=[]
    for emp in employees:
        print(emp.get("id")) #can also remove emp if he/she is not available
        emp['projectid']=""
        emp['matchScore']=0
        if not(emp['available']):
            itemToRemove.append(emp)
    for item in itemToRemove:
        employees.remove(item)

    priorityWiseProject=getpriorityWiseProject(projects)
    # print(priorityWiseProject)
    tempScore=0
    tempprojectId=''
    for project in priorityWiseProject:
            for employee in employees:
                for skill in employee.get('skills'):
                    if skill in project.get("requiredSkills"):
                        tempprojectId=project.get('id')
                        tempScore+=1
                if(tempScore>employee.get('matchScore')):
                    employee['projectid']=tempprojectId
                    employee['matchScore']=tempScore
                tempScore=0
                tempprojectId=""
            # print(employees)
            tempList=[]
            employees=sorted(employees,key=lambda employee:employee["matchScore"],reverse=True)
            for employee in employees:
                print(employee.get('id'))
                if project.get("numPeopleRequired")>0 and employee.get("matchScore") > 0 and project.get("id")==employee.get('projectid'):
                    projectAssignedToEmployeeList.append(employee)
                    # employees.remove(employee)
                    project["numPeopleRequired"]-=1
                else:
                    employee['projectid']=''
                    employee['matchScore']=0
                    tempList.append(employee)
            employees=tempList
            #now scan the employees and get the max matchscore from employee and select as number is required from the project if did not match the required number then project will be unassigned and person without projectid willalso be unassigned
    # print(projectAssignedToEmployeeList,employees)
    projectAssignments={}
    for employee in projectAssignedToEmployeeList:
        if not (employee["projectid"] in projectAssignments):
            projectAssignments[employee["projectid"]]=[employee['id']]
        else:
            projectAssignments[employee["projectid"]].append(employee['id'])
    unassignedEmployees=[]
    for employee in employees:
        unassignedEmployees.append(employee.get('id'))
    unstaffedProjects=[]
    for project in projects:
        if not(project.get('id') in list(projectAssignments.keys())):
            unstaffedProjects.append(project.get('id'))
    return{
        "projectAssignments":projectAssignments,
        "unassignedEmployees":unassignedEmployees,
        "unstaffedProjects":unstaffedProjects
    }

# {
# projectAssignments: {
# P1: ["E1", "E3"],
# P2: ["E4", "E5"]
# },
# unassignedEmployees: ["E2"],
# unstaffedProjects: ["P3"]
# }


def getpriorityWiseProject(projects):
    projects=sorted(projects,key=lambda project :project['priority'])
    return projects

print(assignProject(employees,projects))