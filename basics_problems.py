# ### performing basic arithmetic operations ###
# a = 3
# b = 2
# print(f'sum of two no\'s are {a+b}')
# print(f'sub of two no are {a-b}')
# print(f'product of two no are {a*b}')


# ### performing basic comparison operators ###
# n = int(input('enter no:'))

# if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
#     print('Weird')
# elif (n % 2 == 0 and n > 20) or (n % 2 == 0 and 2 <= n <= 5):
#     print('Not Weird')

#  # task :
#  # The provided code stub reads an integer,n , from STDIN.
#  #  For all non-negative integers i<n , print i^2 .

# no = int(input('enter no:'))

# for no in range(no, 0, -1):
#     print(no*no)


# ## Leap year code ##

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         return False


# year = int(input('enter year:'))

# if is_leap_year(year):
#     print('leap year')
# else:
#     print('not a leap year')


# # task:Given the participants' score sheet for your University
# # Sports Day, you are required to find the runner-up score.
# # You are given  scores.
# # Store them in a list and find the score of the runner-up.
# list = [1, 2, 9, 10, 8, 3]

# sorted = list.sort(reverse=True)  # list returns none
# i = 0
# for no in list:
#     if i == 1:
#         print(f'{no} is runner up score')
#     else:
#         pass
#     i += 1

# # checking a no is prime or not


# def is_prime_no(num):
#     if num <= 1:
#         return False
#     else:
#         for no in range(2, int(num**0.5)+1):
#             if num % no == 0:

#                 return False

#     return True


# integer = int(input('Enter any no:'))

# accept = is_prime_no(integer)

# if not accept:
#     print('it is not a prime no')
# else:
#     print('it is a prime no')

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def fun(self):
#         return (f'''Hello, my name is {self.name} and marks
#                 are {self.marks[0]},
#                 {self.marks[1]},{self.marks[2]}''')


# stu1 = student('manav', [88, 99, 100])
# stu2 = student('kunal', [88, 99, 100])
# print(stu1.fun())

# Task:Both players are given the same string, .
# Both players have to make substrings using the
# letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all
# possible substrings.
# Scoring:
# A player gets +1 point for each occurrence of the
# substring in the string .
# def minion_game(word):
#     kevin = 0
#     stuart = 0
#     vowels = "AEIOU"

#     for i, ch in enumerate(word):
#         points = len(word) - i

#         if ch in vowels:
#             kevin += points
#         else:
#             stuart += points

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif stuart > kevin:
#         print("Stuart", stuart)
#     else:
#         print("Draw")


# word = input("Enter a word: ").upper()
# minion_game(word)


# swap_case #


# def swap_fun(character):
#     strin = ''
#     for i, ch in enumerate(character):
#         if ch.islower():
#             convert_upper = ch.upper()
#             strin += convert_upper
#         else:
#             convert_lower = ch.lower()
#             strin += convert_lower
#     return strin


# inp = input('enter any string:')
# new_str = swap_fun(inp)
# print(new_str)

# list problem #
# common operations on list
# def list_cmd(n):
#     list = []
#     print(f'{n} no of commands will be performed')
#     list.insert(0, 5)
#     list.insert(1, 6)
#     list.insert(2, 8)
#     list.insert(3, 9)
#     print(list)
#     list.remove(5)
#     list.append(7)
#     list.sort()
#     list.pop()
#     list.reverse()
#     print(list)


# inp = 11
# list_cmd(inp)

## nested list ##

lis = [['manav', 99], ['rahul', 22], ['karan', 33], ['arnav', 22],
       ['shelly', 33]]
sorted_list = []
name_list = []
count = 0
second_lowest_marks = []

for i in lis:
    sorted_list.append(i[1])  # here we are appending marks of
    # all students in a list.
    name_list.append(i[0])  # here we are appending students name
sorted_list.sort()

sorted_list = list(set(sorted_list))
sorted_list.sort()

# sorting marks ascending order
print(sorted_list)

for i in sorted_list:
    if count == 1:
        second_lowest_marks = sorted_list[1]  # here we are assigning
        # second lowest grade to new list
    count += 1

for name in lis:
    if second_lowest_marks == name[1]:
        print(f'''the person who has lowest score is {name[0]}
               which is {name[1]}''')
