luv = 'Here, have a hug free on the house!'
justincase = 'Take a hug, just in case you need it later.'
hurts = ('sad', 'depressed', 'unhappy', 'lonely', 'alone', 'isolated', 'crappy',
'Sad', 'Depressed', 'Unhappy', 'Lonely', 'Alone', 'Isolated', 'Crappy')
friendsquery = 'Enter a one word answer in response to the question.'
HowRU = 'How are you? '

import time

print(friendsquery)
time.sleep(3) #seconds
feelings = input(HowRU)
time.sleep(1) #seconds

if hurts.__contains__(feelings) == True:
    print(luv)
else:
    print(justincase)
