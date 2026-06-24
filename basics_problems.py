### performing basic arithmetic operations ###
a = 3
b = 2
print(f'sum of two no\'s are {a+b}')
print(f'sub of two no are {a-b}')
print(f'product of two no are {a*b}')


### performing basic comparison operators ###
n = int(input('enter no:'))

if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
    print('Weird')
elif (n % 2 == 0 and n > 20) or (n % 2 == 0 and 2 <= n <= 5):
    print('Not Weird')

 # task :
 # The provided code stub reads an integer,n , from STDIN.
 #  For all non-negative integers i<n , print i^2 .

no = int(input('enter no:'))

for no in range(no, 0, -1):
    print(no*no)


## Leap year code ##

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


year = int(input('enter year:'))

if is_leap_year(year):
    print('leap year')
else:
    print('not a leap year')


# task:Given the participants' score sheet for your University
# Sports Day, you are required to find the runner-up score.
# You are given  scores.
# Store them in a list and find the score of the runner-up.
list = [1, 2, 9, 10, 8, 3]

sorted = list.sort(reverse=True)  # list returns none
i = 0
for no in list:
    if i == 1:
        print(f'{no} is runner up score')
    else:
        pass
    i += 1

# checking a no is prime or not


def is_prime_no(num):
    if num <= 1:
        return False
    else:
        for no in range(2, int(num**0.5)+1):
            if num % no == 0:

                return False

    return True


integer = int(input('Enter any no:'))

accept = is_prime_no(integer)

if not accept:
    print('it is not a prime no')
else:
    print('it is a prime no')
