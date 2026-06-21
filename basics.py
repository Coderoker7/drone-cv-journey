## learning basics of python ##
## strings ##

name = ' Manav Dobriyal '
dob = '23_twenty_three_oct'

print(name)
print(dob)
length = len(name)
print(name[3])
print(length)
print(name[0:4])

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
