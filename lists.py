numbers = [1, 2, 3, 4]
names = ["Aman", "Rahul","Rahuls", "Neha", "10"] #Lexicographical order
names.sort() #Ascending order
print(names)
names.sort(reverse=True) #Descending order
print(names)
mixed = [1, "Python", 3.5, True]
print(names[0])
print(names[-1])
names[1] = "Rohit"
print(names)

# List Methods Examples
a = [1, 2, 3]
a.append(4)
print(a)
a.extend([5, 6])
print(a)
a.insert(0, 0)
print(a)
a.remove(0)
print(a)
popped = a.pop(5)
print(popped)
print(a)
b = [1, 2]
b.clear()
print(b)
print(a.index(3))
print(a.count(2))
c = [3, 1, 2]
c.sort()
c.reverse()
d = a.copy()