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

a = 1.1
print(type(a))
