#1
x = 123.456789
print(x)
print(f'{x:.3f}') #print float number, 3 decimal places, round if necessary
print(f'{x:.5e}') # print exponential number, 3 demical places, round if necessary
print(f'{x:.4%}') # print percentage, 3 demical places, rounds if necessary

#2
s = 'hello world'
print(s.upper())
s = 'HELLO WORLD'
print(s.lower())
s = 'hello world'
print(s.title())
s = 'hEllO WorLD'
print(s.swapcase())

#3
s = 'Nguyen, Duc, Trung, GCH220848'
a = s.split(',') #convert string to list
print(len(a))

b =' '.join(a)   #convert list to string
print(b)

#4
s = 'hello python world'
teen_s = s.replace('o','O').replace('e','3').replace('l','1')
print(teen_s)

# String operators: +, *
s = 'hello' + ' ' + 'world'
print(s)
s = 'hello ' * 3
print(s)

#6
s = 'hello world'
print(s[:5])
print(s[-5:])

#7
colors = ['red','green','blue','yellow']
if 'red' in colors:
    print('red is in the list')
if 'black' not in colors:
    print('black is not in the list')
    
#8
name = 'Trung'
new_name = input('enter name')
new_name = name
print(name)

#9
numbers = [1,2,3,4,5,6,7,8,9,10]
a = numbers[0:5]
print(a)
b = numbers[3:8]
print(b)
c = numbers[0:8:3]
print(c)
a = numbers[:5]
print(a)
c =numbers [:5:2]
print(c)
d = numbers[6:10]
print(d)
d = numbers[6:]
print(d)
e = numbers[5::2]
print('t: ',e)
f = numbers[::]
print(f)
g = numbers[::2]
print(g)
h = numbers[1::2]
print(h)

#10
print("hello", end = ' ')
print('world')
