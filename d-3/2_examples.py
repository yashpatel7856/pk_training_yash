# 1 age
# age=int(input("enter your age"))
# if age<10:
#     print("child")
# elif age<20:
#     print("teenager")
# elif age<30:
#     print("young")
# else:
#     print("old")


# 2 prime number

for i in range(1,20):
    for j in range(2,i):
        if i%j==0:
            print(i,"is not a prime number")
        else:
            print(i,"is a prime number")
        break