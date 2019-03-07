#print a message 10 times

'''

count = 0
while count <10:
    print('inside loop')
    count += 1

#search for a value in a list
found = False

'''

'''
answer = 7
num = 0
#input a number

while num != answer:
    num = input('enter a number')
    num = int(num)
    if num == answer:
        print('you got it') 
    elif num > answer:
        print('too big')
    else:
        print('small')

#loop while that number is nois not iqual your answer

#if the input is bigger print too big

#if the input is smaller print too smal

#if the input is right break and print you got it



'''

'''
answer = 7
user_in = 0

while answer != user_in:
    user_in = int(input("Enter a number: "))
    if user_in > answer:
        print("Number {} is too big!".format(user_in))
        break
    elif user_in < answer:
        print("Number {} is too small!".format(user_in))
        break
    else:
        print("Number {} is the number!".format(user_in))
        break



'''


#find a sum of a list

ages = [25, 39, 45, 41, 27, 18, 33, 65, 11, 50]

count = 1
x = ages[0]
y = ages[count]
z = x + y
while count != 10:
    count = count + 1
    y = ages[count]
    z = z + y
print(z)

# total_age = 0
# for age in ages:
#     total_age += age

# print(total_age)
