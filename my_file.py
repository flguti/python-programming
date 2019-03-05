# note = 70
# if note > 79:
#     print('A')
# elif note < 60:
#     Print('C')
# else: 
#     print('B')

import random

y = input("Enter your number")
y = int(y)
x = random.randint(1,2)
if x == y:
    print('correct')
else:
    print(x, 'try again')

