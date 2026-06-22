a = 3
b = 2
print(f'sum of two no\'s are {a+b}')
print(f'sub of two no are {a-b}')
print(f'product of two no are {a*b}')

n = int(input('enter no:'))

if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
    print('Weird')
elif (n % 2 == 0 and n > 20) or (n % 2 == 0 and 2 <= n <= 5):
    print('Not Weird')
