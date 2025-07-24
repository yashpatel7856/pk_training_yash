
############################################   string ###################################################
# str="hello world {}"
# print("%d the string is %s"%(15,str))
# print(str[:6][:3])
# l1=list(str)
# print(l1)
# print(''.join(l1))
# print(str.format('new user'))
# item1=1000
# item2=500
# print(f'total price{item1+item2}') #<-fstring  we can also use "string template" "hello $name"  and then str.substitute(name="new user")


#find vowelin string
# str="this is just a normal string with multiple alphabets"
# vowels="aeiou"
# count=0
# for a in str:
#     if a in vowels:
#         print(a)
#         count+=1
# print(count)


#convert binary to int
# str='101'
# for a in ''.join(str.split('').reverse()):
#      print(a)

# def convertToInt(str):
#     for a in str:
#         if a not in '01':
#             print("given string is not in binary form")
#             return
#     return int(str,2)
# print(convertToInt(str))


# remove all digits from string
# obj="hello564 world657 and something with 0000"
# def removeDigits(obj):
#     digits=[str(x) for x in range(0,10)]
#     str2=[]
#     for c in obj:
#         if c not in digits:
#             str2.append(c)
    
#     return ''.join(str2)

# print(removeDigits(obj))

#Python program to sort the characters in a string
# str1="this is the example string to sort"
# def sortCharInStr(string):
#     list1=list(string)
#     list1.sort()
#     for x in list1:
#         if x==" " or not(x.isalpha()) :
#             list1.remove(x)
#     return list1
# print(sortCharInStr(str1))


# Python program to remove duplicate characters from a string
# def removeDups(string):
#     list1=list(string)
#     dups=[]
#     for x in list1:
#         if x not in dups:
#             dups.append(x)
#     return ''.join(dups)
# print(removeDups("someethingos"))



# Python program to list unique characters with their count in a string
# def countchar(string):
#     dict={}
#     list1=list(string)
#     for x in list1:
#         if x not in dict:
#             dict[x]=1
#         else:
#             dict[x]+=1
#     return dict
# print(countchar("somestringwithsamechar"))



# Python program to find number of words in a string
# def countWord(string):
#     list1=string.split(' ')
#     return len(list1)
# print(countWord("this is a example string to count words"))


# Python program to remove all non-alphabetic characters from a string
# def trimNonAlpha(string):
#     list1=list(string)
#     # print(list1)
#     for x in list1:
#         # print(x)
#         if not(x.isalpha()):
#             list1.remove(x)
#             print(len(list1))
#     return ''.join(list1)
# print(trimNonAlpha("this\n is @ exa3mple1 strin3g of &n3o&n 11"))


############### updating number of elements in list while iterating #################
# a = [1,2]
# i = 0
# for item in a:
#       if i<5:
#           print ('append')
#           a.append(i+2)
#       print (a)
#       i += 1



##################################     list            #############################


# list1=[1,2,3]
# list2=[4,5,6]
# indices=range(len(list1))
# for x in indices:
#     print(x)

# combinedList=[(x,y) for x in list1 for y in list2 if x*y%2==0]
# newlist=[]
# for (x,y) in combinedList:
#     newlist.append(x*y)
# print(newlist)

# list3=[" ","abc","deg"," ","yzh" ]
# list3.sort()
# print(list3)

# list3=list(list1) #to copy list use list(),sliceing operator[start:end:step],copy.copy(shalow copy),copy.deepcopy(deep copy),
# list3[0]=100
# print(list1)
# print(list3)


# Python program to find unique numbers in a given list.
# list1=[1,2,3,4,3,1,5,6,76,7,8,7,3,2]
# def uniqueNums(list1):
#     dups=[]
#     for x in list1:
#         if x not in dups:
#             dups.append(x)
#     return dups
# print(uniqueNums(list1))


# Python program to find sum of all numbers in a list.
# list1=[1,2,3,4,3,1,5,6,7,8,7,3,2]
# def sumOfList(lsit1):
#     sum=0
#     for x in list1:
#         sum+=x
#     return sum
# print(sumOfList(list1))


# Python program to create a list of 5 random integers.
# import random
# def getRandomNumList(length):
#     count=0
#     list1=[]
#     while count<length:
#         list1.append(random.random()) # can also use randint
#         count+=1
#     return list1
# print(getRandomNumList(5))



################################  Tuple #######################################

# tup1=(50,) # if comma is not included then tup1 with only one element will be treated as int value
# print(type(tup1))

# T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
# t2=()

# for x in T1:
#     if x not in t2:
#         t2+=(x,) # concatination

# print(t2)

# tup1=(10,20,30)
# x,y,z=tup1
# print(x,y,z)


##############################3 set #############################

# myset={1,2,3,4,3,5}
# myset={1,"hello",(1,2,3)} # can add only immutable elements in set 
# myset.add(7)
# # myset.remove(8)
# # myset.discard(8) # does not throw error if element is not present 
# print(myset.pop())
# myset.remove("hello") #set.discard
# myset.clear()
# print(myset)


# set1={1,2,3,4,5}
# set2={4,5,6,7,8}

# for x in set1:
#     if x in set2:
#         print(x)

# print(set1&set2) # & intersection
# print(set1|set2) # | Union
# print(set1-set2)



###################################  dictionary ##################################3

# dic={"hell":"oo",(1,2):[1,2,3,4,45]}  # keys can be string number or tupple it can not be set list
# print(dic.keys())
# for c in dic.keys():
#     print(type(c))


# print(dic.get("hell"))
# dic.setdefault("some","value")
# print(dic.get('adish'))


# Using square brackets []
# Using the update() method can add multiple keys and their value
# Using a comprehension
# Using unpacking newdict={**dict1,**dict2}
# Using the Union Operator ==> dict1 | dict2
# Using the |= Operator  dict1 |= dict2
# Using setdefault() method 
# Using collections.defaultdict() method

# dic2=dic
# print(dic2['hell'])

# Python program to create a new dictionary by extracting the keys from a given dictionary.
# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
# keys = ['two', 'five']
# def copyGivenKeys(keys,dict):
#     newdict={}
#     for key in dict:
#         if key in keys:
#             newdict[key]=dict[key]
#     return newdict
# print(copyGivenKeys(keys,d1))

# to remove keys with same values

# Python program to sort list of dictionaries by values
# dic={
#     "one":3,
#     "two":"string",
#     "three":[1,2,3,4,5,6,7],
#     "seven":5,
#     "four":(1,2,3,4,5),
#     "five":{"set"},
#     "six":4
# }
# dic2={}
# print("345".isnumeric())

# for key,value in dic.items():
#     if str(value).isnumeric():
#         dic2[key]=value
    
# print(dic2)


#Python program to build a dictionary from list of two item (k,v) tuples.

# list=[(1,2),(3,4)]
# dict={}
# dict.update(list)
# for x,y in list:
#     dict.update(x,y)
# print(dict)
# dict2={7:8,9:0}
# dict3={**dict,**dict2}
# print(dict3)




###########################   try ########################################3
# try:
#     file=open('foo.txt','r+')
#     print(file.readline())
# except IOError as err:
#     print(f'error occured {err}')
# else:
#     print('inside the else block')
# finally:
#     print('this will always work')


################3333  recursion #############

# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num * factorial(num-1)
# print(factorial(5))

#####################################   time     `` ############################3

# import time
# dic=time.localtime()
# print(dic)
# print(dic.tm_year)


# import calendar
# print(calendar.isleap(2025))
# cal=calendar.month(2025,7)
# print(cal)

from datetime import datetime

dt=datetime.now()

print(dt.date)