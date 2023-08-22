
#while loop
'''while condition:
        code     '''

count = 0
while  count < 3:
    print('Hello')
    count += 1
    
age = True
while age:
    user_age = int(input('How old are you?' ))
    if user_age < 18:
        age = False
        
#ForLoop
output = ''
for i in range(3): #start from index 0
    output += '*'
print(output)

for i in range(1,4): #start from 1 to 3
    print('Trung')
    
for i in range(1,10,2): #start from 1 to 9 with step is 2
    print(i)
    
for i in range(10,1,-2):
    print(i)
    
text = 'My name is Trung'
#print(text[])
for letter in text:
    print(letter)

#break
import random
computer_number = random.randint(1,10)
time = 0
while True:
    user_guess = int(input('Enter your number: '))
    time += 1
    if user_guess == computer_number:
        break
print(f'You win after {time} guesses  \nComputer number is: {computer_number} and your number is: {user_guess}')


#continue
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
    
#nested loop
number_1 = int(input('Enter your number 1: '))
number_2 = int(input('Enter your number 2: '))

common_divisor = 1
for i in range(1, number_1 + 1):
    if number_1 % i == 0:
        for j in range(1, number_2):
            if number_2 % j == 0 and i == j:
                common_divisor = i

print(common_divisor)

#nested loop to print mutiplication table
size_table = 10

for i in range(1, size_table + 1):
    for j in range(1, size_table + 1):
        result = i * j
        print(f'{result:3}', end = ' ' )
    print()

