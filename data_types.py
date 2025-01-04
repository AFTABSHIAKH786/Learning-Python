#String 
print("Hello");
name = "Aftab"
print(name);

#numbers
age = 22;
print(age)

#boolean
is_Lazy = True
print(is_Lazy);

#These where primitive data types Now we will see Advance Datatypes

#List also can be said as array
myList  = [1,2,3,"Hello", "world", 4,5,6]
print(myList)

#Tuples once defined it cannod be changes or mutated
myTuple = (1,2,3,4,"Hello")
print(myTuple)

#Dictionary key value pair.
myDict = {
    "name": "Aftab",
    "age": 22,
}
print(myDict)
print(myDict["name"])

#sets similer to the sets that we learned in class 12th 
mySet = {1,2,3,4}
#now we can to set operations in the above set such as AND and OR operations
print(mySet & {1,3}) 
print(mySet | {4,5,6,7})

#Boolean Ture and False are often treated as 1 and 0 so there are some bizzare operations happens as well 
print(True + 1) #This will retrun 1 + 1 = 2 
print(False - 1) #This will return 1 - 1 = 0

# There are more data types availabe too for python but its better to learn them while applying them into relevent projects to have a great project based learning

