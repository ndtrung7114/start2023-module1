#1
x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)

#2
radius = float(input('Enter radius: '))
if radius >= 0:
    area = radius * radius * 3.14159
    print(f"The area for the circle of radius {radius} is {area}")
    
#3
radius = float(input('Enter radius: '))
if radius >= 0:
    area = radius * radius * 3.14159
    print("The area for the circle of radius", radius, "is", area)
else: 
    print("Negative input")
    
#4
#calculate BMI
height = float(input('Enter your height (m) '))
weight = float(input('Enter your weight (kg) '))
formula = (weight) / (height) ** 2
if formula < 18.5:
    print('You are underweight. ')
elif 18.5 < formula < 24.9:
    print('You are normal. ')
elif 25 < formula < 29.9: 
    print('You are overweight. ')
else:
    print('Obese')
    
#5
score = float(input('Enter your score'))

if score > 4:
    print("Passed")
if score > 6:
    print("Passed")

#6
num = int(input('Enter your number: '))
print('This is even number 'if (num % 2 == 0) else 'This is odd number')



