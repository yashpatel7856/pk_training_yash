# Problem 5: Online Course Platform with Instructors, Enrollments, and Rating System

# Problem Statement:

# Build an online learning system with these requirements:

# Course has: title, instructor, capacity, enrolled students, ratings.
# User can enroll in courses and leave a rating.
# Instructors can view average ratings for their courses.
# Do not allow overbooking beyond course capacity.

# Sample Input
# python
# c1 = Course("Python Bootcamp", "Alice", 2)
# u1 = User("Bob")
# u2 = User("Eva")

# u1.enroll(c1)
# u2.enroll(c1)
# u1.rate_course(c1, 5)
# u2.rate_course(c1, 4)

# c1.get_average_rating()

# Sample Output
# User Bob enrolled in Python Bootcamp
# User Eva enrolled in Python Bootcamp
# Average rating for Python Bootcamp: 4.5

# start time : 12:37
# end time :  1:30


class Course:
    def __init__(self,name,instructorName,capacity):
        self.name=name
        self.instructorName=instructorName
        self.capacity=capacity
        self.avrageRatings=0
        self.ratings=[]
        self.enrolledUsers=0
    def get_average_rating(self):
        print(f'avrage rating of course {self.name} : {self.avrageRatings}')
        return self.avrageRatings
    def updateAvrageRating(self,rating):
        self.ratings.append(rating) 
        if self.avrageRatings==0:
            self.avrageRatings=rating
        else:
            sum=0
            for x in self.ratings:
                sum+=x
            self.avrageRatings=(sum)/len(self.ratings)
    def addUser(self,count):
        self.enrolledUsers+=count
    def canEnrollCourse(self):
        if self.enrolledUsers<self.capacity:
            return True
        else:
            False   


class User:
    def __init__(self,name):
        self.name=name
        self.enrolledCourses={}
    def enroll(self,course):
        if course.canEnrollCourse():
            course.addUser(1)
            if course.name not in self.enrolledCourses:
                self.enrolledCourses[course.name]={"rating":0,"info":"some other data"}
                print(f'User {self.name} enrolled in course {course.name}')
            else:
                print(f'{self.name} already enrolled in course {course.name}')
        else:
            print(f'course capacity reached can not join course')
    def rate_course(self,course,rating):
        if rating < 0 or rating >10:
            print(f'give rating between 0/10 user={self.name},course={course.name},invalid value="{rating}"')
            return
        if course.name in self.enrolledCourses:
            
            course.updateAvrageRating(rating)
            self.enrolledCourses[course.name]["rating"]=rating
        else:
            print(f'{self.name} is not enrolled in course.enroll first to review')

c1 = Course("Python Bootcamp", "Alice", 5)
u1 = User("Bob")
u2 = User("Eva")
u1.enroll(c1)
u2.enroll(c1)
u1.rate_course(c1, 2)
u2.rate_course(c1, 8)

c1.get_average_rating()