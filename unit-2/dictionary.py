'''

my_list = []


# add to my_list
# append(), insert()

# remove from list
# pop(),  remove()

#ordered, mutable

#dictionaries

students = {}

#add to dictionaries
students['name'] = 'John'

print(students)

students['name'] = 'Marthe'

print(students)

students['courses'] = ['Python programming', 'Data Science', 'UX', 'Social Media Marketing']

print(students)

students['courses'].append('Web Developmemt')

print(students)

'''
'''

#model a playlist
my_playlist = []

#each song on playlist
#genres - list
#artists - list
#albun - string
#release_year - string
#title - string
#playback_length - string
# - dictionary

my_song = {
    'genres' : ['pop', 'rock'],
    'artists' : ['Jimmy Page', 'Robert plan'],
    'albun' : 'Led Zepelin 4',
    'release_year' : '1978',
    'title' : 'Startway to haven',
    'playback_length' : '10:05'
}

my_playlist.append(my_song)

print(my_playlist)
'''
'''
#pass by reference
def swap_first_two(my_list):
    my_list[0], my_list[1]] = my_list[1], my_list[0]

    # x = my_list[0]
    # y = my_list[1]
    # my_list[0] = y
    # my_list[1] = x

a_list = [1, 2, 15, 20]
swap_first_two(a_list)

print(a_list)
'''
#Gutierri

my_name = {
    'g': 1,
    'u': 1,
    't': 1,
    'i': 2,
    'e': 1,
    'r': 2
}

# def frequency_generator(a_string):
#     for x in len(a_string):

# for item in my_name.keys():
#     print('the letter {} appears in my name {} times'.format(item, my_name[item]))

# for letter, val in my_name.items():
#     print('the letter {} appears in my name {} times'.format(letter, val))

#word frequency generator
def frequency_generator(a_string):
   #returns the number of times each word
   # appears i a string
   for x in len(a_string):


#my_sentence = 'There is a man with a plan. The man has a plan in hand'
#frequency_generator(my_sentemce)
# There:1
# is:1
# a:3
# man:2
# with:1
# plan:2
# has:1
# in:1
# hand:1
