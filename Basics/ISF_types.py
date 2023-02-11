grades = [9, 8.1, 6, 5.5, 7.1]

gradesum = sum(grades)
count = len(grades)
average = gradesum / count

highestgrd = max(grades)

print(average.__int__())
print(highestgrd)
print('break')

for grade in grades:
    print(round(grade))

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has a number {}".format(key, value))

number = "+456"
print(number.replace('+', '00'))

while isinstance(number, str):
    print(number)