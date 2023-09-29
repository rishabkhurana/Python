"""
dictionary
-> represent a group of objects as key-value pairs.
-> duplicated keys are not allowed but values can be duplicated.
-> intersection order is not preserved.
-> they are mutable and dynamic.
-> indexing and slicing are not applicable.
"""
d = {}
print(type(d))

d[1] = "Rishab"
d[2] = "akshat"
d[3] = "arjun"
print(d)
print(d[3]) #we can access data by using keys. If the key is present then it shows Key Error:400

rec = {}
n = int(input("Enter number of students: "))
i = 1
while i<=n:
    name = input("Enter the students name: ")
    marks = input("Enter %/ of marks of student ")
    rec[name] = marks
    i = i+1
    print("name of Student","\t","%/ of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])

#d[key] = value --> used to update dictionaries.

#functions of Dictionaray
#1. dict() --> to create dictionary
#2. len() --> Returns the number of items in the dictionary
#3. clear() --> to remove all the elements from the dictonary
#4. get() --> to get the value associated with the key. for eg: (d.get(key,default value))
#5. pop() --> it removes the entry associated with the specified key and return the corresponding value. for eg: d.pop(key)
#6. popitem() --> it removes an arbitary item.
#7. keys() --> it returns all keys associated with dictionary
#8. values() --> it returns all values associated with the dictionary
#9. setdefault() --> if key is already available then this function returns the corresponding values
#10. update() --> all items present in the dictionary X will be added to dictionary d