def introduce(name, age):
    print(f'Hello everyone my name is {name} \n Im {age} years old')

introduce('T', 18)
introduce('R', 17)
introduce('U', 16)
introduce('N', 15)
introduce('G', 14)


def sum(a, b):
    result = a + b
    return result
   

print(sum(10, 20))


def display(something, n = 3):
    for i in range(n):
        print(something, end = ' ')
display('Trung', 4)


def subtraction(a, b):
    result = a - b
    return result
print(subtraction(5, 2))
print(subtraction(2, 5))


def calculate_rectangle(length, width):
    c = 2
    perimeter = (length + width) * 2
    area = length * width
    return perimeter, area

perimeter = 20
c = 3
print(perimeter)

perimeter, area = calculate_rectangle(5, 2)
print(perimeter)

