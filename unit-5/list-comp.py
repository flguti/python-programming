marvel_movies = ['Captain America, The First Avenger', 'Iron Man', 'Iron Man II',
'Thor', 'Thor, The Dark World', 'The Amazong Spiderman', 'Dr Strange']

'''
create a new list with all the movies without the word 'The' in their title
'''

new_list =[]
for name in marvel_movies:
    if 'The' in name:
        pass
    else:
        new_list.append(name)


#print(new_list)

#list comprehension
#list comprehension
new_movies = [movie for movie in marvel_movies if 'The' not in movie]

print(new_movies)


#copy old list
fruits = ['apple', 'peach', 'mango']
           #result
copy_fruit = [fruit for fruit in fruits]
                   #___________________
                   #iteration

numbers = [2,46,8,10]
new_numbers = [num ** 2 for num in numbers]

print(new_numbers)

vals = [1, 2, 3, 5, 7, 9, 11]
odds = [val for val in vals if val % 2 == 1]

print(odds)

nice_fruit = ['Apple', 'Peaches', 'Pear', 'Mango', 'Kiwi']

new_fruit = [ fruit if fruit[0] == 'P' else fruit[0] for fruit in nice_fruit ]

print(new_fruit)