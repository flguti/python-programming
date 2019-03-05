classmates = ["Ros", "Marcus", "Flavio", "Joseph", "Maham", "Vinay", "Gungeet", "Faris"]

#prints the number of Items
print(len(classmates))

#prints the first item in the list
print(classmates[-1])

#add an element to the list
classmates.append("John")

#adding an element 
classmates.insert(1, "Jane")

#remove elements
classmates.pop()

#print all elements in the list
for name in classmates:
    print(name)

#search for item in list
for name in classmates:
    if name == 'Maham':
        print('Maham found in list')

if 'Maham'in classmates:
    print('found Maham in list')

name = 'lopes'
for x in range(-1, -6, -1):
    print(name[x])

print(name[::-1])


print(classmates)