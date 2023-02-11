#user_in = input('Enter your name:')
#user_in1 = input('Enter your surname:')
#when = 'today!'

#message = 'Hello %s %s' % (user_in, user_in1)
#message1 = f'Hello {user_in} {user_in1}. Whats up {when}'
#print(message1)

def name(fname):
    cfname = fname.capitalize()
    return 'Hi %s' % (cfname)
    
fname = input("Enter First Name:")
print(name(fname))

def temps(inte):
    return inte + 1

temp = [21.1, 22, 13, 4]

for tempa in temp:
    print(temps(tempa))