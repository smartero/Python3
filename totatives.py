
'''
Totatives 
In number theory, Euler's totient function (phi function) counts the positive integers up to a given integer n that 
are relatively prime to n. Two integers are said to be relatively prime if the only positive integer (factor) 
that divides both of them is 1. The numbers less than or equal to and relatively prime to 
a given number n are called totatives. 
For example: 
Input: 9 
Output: 6 
(The totatives of n = 9 are six numbers 1, 2, 4, 5, 7 and 8, so phi(9) = 6 because 3, 6 and 9 are not relatively prime with 9) 
Note that, phi(1)=1 because 1 is considered to be relatively prime to every positive number. 
Write a program to take positive integer n as an input and print 
the number of totatives in the numbers less than or equal to n.
'''
while True:
    print('Input positive number:')
    try:
        x = int(input())
    except:
        print('Please input number')
    if x >=1:
        break

numbers_excl = set()
numbers = []
for number in range (1,x):
    for y in range (2, x):
        if x % y == 0 and number % y == 0:
            numbers_excl.add(number)
numbers = [x for x in range(1, x) if x not in numbers_excl]
if 1 not in numbers:
    numbers.append(0, 1)
print('phi({}) - {} // {}'.format(x, len(numbers), numbers))
