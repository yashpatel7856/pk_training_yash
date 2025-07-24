# file=open('foo.txt',"r")
# print(file.name,file.closed,file.mode)
# print(len(file.readlines()))

# with open('foo.txt','r') as file:
#     line=file.readline()
#     while line :
#         print(line)
#         line=file.readline()

# with open("foo.txt",'wb') as file:
#     # file.writelines(['newdata in file\n','something in secind line\n','last line\n'])
#     file.write('some line \n')
#     file.write('again something')

# with open("foo.txt",'r+') as file:
#     # file.write('some line \n')
#     # file.seek(11)
#     # file.write('after seek')
#     file.seek(0)
#     data=file.read(5)
#     print(data)


import os

# os.rename("foo.txt","example.txt")
# os.remove("example.txt")
# print(os.getcwd())
# os.makedirs('example') #creates only if it doesnot exists
# os.mkdir(os.getcwd()+'\example\inside_example')
# try:
#     for x in os.listdir('./'):
#         if not(x.index('.py')) and os.path.exists(x):
#             print(os.listdir(x))
# except OSError as e:
#    print(f"Error: Failed to list contents of directory . {e}")


# print(os.listdir())
# os.chdir('example')
# print(os.getcwd())
# print(os.listdir())
# os.rmdir('D:\\PK_training\\d-4\\example',)

# with open('foo.txt','r+') as file:
#     for a in range(5):
#         print(file.next())

# print(os.path.abspath('..\\d-4'))
# print(os.path.isdir(os.path.abspath('..\\d-4\\example')))

