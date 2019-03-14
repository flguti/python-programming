#message 

# def message(*)



# keyword arguments

# def say_hi(name, job='instructor'):
#     print('Hello {}, your\'re an {}'.format(name, job))

# say_hi('Maham')
# say_hi('Maham', job='dev')
# say_hi('Maham', 'flavio')

#dictionary is a collection of keyvalue pair




# people = {'Bob': 'Engineer', 'Alice': 'Lawyer'}

# print(people.keys())
# print(people.values())
# print(people.items())

# def say_hello(**kwargs):
#     for key, val in kwargs.items():
#         print('Hello {}, it\'s good that you\'re a {}'.format(key, val)


# say_hello(Bob='Engineer', Alice='Lawyer')


def car_type(**kwargs):
    num_items = len(kwargs)
    if num_items == 3:
        msg = 'Your {} {} is {}, That\'s so cool'.format(kwargs['make'], kwargs['year'], kwargs['color'])
    if num_items == 2:
        msg = 'Your {} is {}, That\'s so cool'.format(kwargs['make'], kwargs['color'])

    print(msg)
 

car_type(make='Subaru', color='black', year='2017')