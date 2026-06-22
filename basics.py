## learning basics of python ##
## strings ##

name = 'Manav Dobriyal'
dob = '23_twenty_three_oct'

print(name)
print(dob)
length = len(name)
print(name[3])  # letter find by index
print(length)
print(name[0:4:2])  # slicing => start:stop:step


### ESCAPE SEQUENCES ###

string_add = 'american \' potato'  # \ is an escape character
# and \n is an escape sequence
# after \ anything come its meaning change
print(string_add)


# formatted strings

name = 'arnav'
sirname = 'ghildiyal'
format = f'my name is {len(name) } and sirname is {sirname}'
print(format)
# inside curly braces we can put any valid expression


### TYPE OF DATA ###
a = 1.1
print(type(a))  # float
print(type(range(4)))  # range(start, stop, step)
print(type('hello'))  # str
print(type([1, 2, 3, 4]))  # list
# list,range,strings are iterable data types


### comparison operators=> if-elif-else ###
# and or not => logical operators

temp = 30
if temp > 30 or temp == 30:
    print('it is hot')
elif temp < 30:
    print('it is cold ')
elif temp >= 30:
    print('it is normal')

person = True
person1 = False
if person:
    print('true')
if not person1:
    print('false')


### Ternary operator ###
age = 19
message = 'eligible' if age > 18 else 'not eligible'
print(message)


### loops ###

for no in range(1, 5):
    print(no, no*'.')

### for else loop ###

sucess = False
for no in range(1, 5):
    print(no)
    if sucess:
        print('sucess')
        break
else:
    print('not sucess')


## Nested loops ##
# firstly inner loop will completely execute then outer
# loop will execute
for i in range(3):
    for j in range(3):
        print(i, j)


## while loop ##
# we use while loop when we dont know how many times
# we have to execute the loop

condition = True
while condition:
    print('hello world')
    condition = False

### Another program ###
print('to stop pls enter no')
word = 'yes'
while word != 'no':
    word = input('enter a word: ')
    print(f'{word}')
    word = word.lower()

    ### Functions ###

# 1.) Function with no argument and no return keyword


def greet():
    print('hello world')


greet()

# 2.) Function with argument and no return keyword


def greet(name, sirname):  # parameters inside when creating a
    # function
    print(f'Hello {name} {sirname}')


greet('potato', 'dobriyal')  # Arguments when calling a function

# 3.) Function with arguments and return keyword


def add(a, b):
    return a+b


result = add(2, 3)  # we can store the return value and
# use it anywhere in the code
print(result)
# by default every function return none if we dont use return
# keyword

## Augmented assignment operator ##
a = 5
a += 2  # a=a+2
print(a)

## *xargs and **kwargs ##


def func(*args, **kwargs):
    print(args)  # tuple of positional arguments
    print(kwargs)  # dictionary of keyword arguments


func(1, 2, 3, 4, 5, name='johny', sirname='depp')
