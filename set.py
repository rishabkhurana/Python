"""
Set
-> unordered collection of data
-> duplicates not allowed
-> indexing & slicing are not allowed
-> represented in curly brackets
"""

a = {10,20,30,40,20} #remove duplicate
b = {10,20,30,"security","raj",40}
print(a)
print(type(b))

c = set() #creating empty set

d = {10,20,"security"}
for  i in d:
    print(i)         #Accessing Elements

#creating set objects
l = [1,2,3,4]
s = set(l)
print(s)

#functions of sets
#1. add(x)
s = {10,20,30}
s.add(40)
print(s)

#2. update(x,y,z,...)
# to add multiple items to the set,
u = {10,20,30}
v = [40,50,60,10]
s.update(l,range(5))
print(u)
"""
we can use add() to add individual item to the set ,
where as we can use update() function to add multiple items to set.
"""

#3. copy()
# return copy of the set.It is cloned.
r = {10,20,30,60}
r1 = r.copy()
print(r1)

#4. pop()
# it removes and return some random element from the set.
t = {40,10,20,70}
print(t)
print(t.pop())
print(t)

#5. remove()
""" 
it removes specified elements of the set,
if the specified element not present in the set then we will get KeyError.
"""
w = {1,2,3,4,5,6,7}
w.remove(2)
print(w)
"""
w.remove(10)   #gives key error because 10 is not present in the set. 
print(w)
"""

#6. discard(x)
# it removes the specified element from the set,
# if the specified element not present in the set then we won't get any error.
x = {9,8,7,6,5}
x.discard(5)
print(x)

#7. clear()
# to remove the elements from the set.
z = {98,87,56}
print(z)
z.clear()
print(z)



# Mathematical Operation on the set
#1. Union() -> (x.union(y)) ,this function is to return all element present in both the sets.
#2. Intersection() -> (x.intersection(y)) ,return common elements present in both.
#3. difference() -> (x.difference(y)) ,returns the element present in x but not in y.