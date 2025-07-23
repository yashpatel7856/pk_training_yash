#Number
var=10 #integer
b=10.4 #float
c=10+6J #complex

#string
str="something new"
# print(str)
# print(str[0])
# print(str[:])
# print(str * 2)


#List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
list[1]=0
# print (list)           
# print (list[0])         
# print (list[1:3])      
# print (list[2:])        
# print (tinylist * 2)    
# print (list + tinylist) #  concatenated lists

#tuple
tuple=1,2,[1,2,3]
# print(type(tuple))
t2=("something",1,2,4,)
# print(t2)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
# tuple[1]=000 imutable
# print (tuple)               # Prints the complete tuple
# print (tuple[0])            # Prints first element of the tuple
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
# print (tinytuple * 2)       # Prints the contents of the tuple twice
# print (tuple + tinytuple)   # Prints concatenated tuples


#byte
b1 = bytes([65, 66, 67, 68, 69])  
# print(b1)   #b defines it is byte type


#dict
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

# print (dict['one'])       # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (tinydict)          # Prints complete dictionary
# print (tinydict.keys())   # type of dict_keys
# print (tinydict.values()) # typeof dict_values

#set  (does not store mutable values(list,tuple) only stores imutable values(number,string))
set={1,2,1,4,5}
# print(set)

#type conversion
# aa= int(3.3) 
# bb=float(3.3)
# cc=str("3.3")
# print(aa,bb,cc)

# membership operator (in , not in )
a2=[1,2,4,4,5,6,7]
# print(2 in a2)
# print(2 not in a2)

#identity operator (checks for references of variable)
a3=[1,2,3,4]
a4=[6,7,8,9]
a5=a3
# print(a3 is a5)
# print(a3 is a4)
# print(a3 is not a5)
# print(a3 is not a4)


#input fromuser 
# name=input("enter name")
# city=input()
# print("name ",name)

# l=int(input("enter heigth"))
# b=int(input("enter bregth"))

# area=l*b
# print(area)


# repr() //object copy/creation does not evaluate the string given can make object using eval().
#str(),print()


#random lib

# import random
# print(random.random())
# print(random.randint(0,100))
# print(random.choice([1,2,3,4,5,6]))
# l1=[1,2,3,4,5,6]
# random.shuffle(l1)
# print(l1)

#
# chai_type="masala chai"
# quantity=2
# order="i ordered {} cups of {}"
# print(order)
# print(order.format(quantity,chai_type))

#split,join
# order=['masala','ginger','green']
# print(" ,".join(order).split(' '))


tea_varieties=['green','herbal','masala','black']
# print(tea_varieties)
# tea_varieties[1:1]=["test","test"] #add element using split
# print(tea_varieties)
# tea_varieties[1:3]=[] #delete elements using split
# print(tea_varieties[1:1])
# print(tea_varieties)

# for tea in tea_varieties:
#     print(tea,end='-->')

# if "oolong" in tea_varieties:
#     print('i have green tea')

# tea_varieties.append("some new type")
# print(tea_varieties)
# # tea_varieties.pop()
# tea_varieties.insert(1,"again some new type")
# print(tea_varieties)
# print(tea_varieties.index("herbal"))

#comp for loop
# sq_num=[x**3 for x in range(10)]
# print(sq_num)

chai_type={
    "masala":"spicy",
    "green":"zesty",
    "black":"unknown"
}
# print(chai_type)
# print(chai_type.values())
# print(chai_type.items())
# print(chai_type.fromkeys(['masala','green'],[['something'],['nothing']]))
# print(chai_type.get('masala'))

# for chai in chai_type:
#     print(chai,chai_type[chai])
# for key,values in chai_type.items():
#     print(key,values)