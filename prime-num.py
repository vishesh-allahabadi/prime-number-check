# prime number
from tkinter import Y


while True:
    num = int(input("enter a number to check if it\'s a prime number ot not: \n"))
    is_prime = True
    for i in range(2, num-1):
        div = num % i
        if div != 0:
            i += 1
        else:
            is_prime = False
            break
    if is_prime == False:
        print(f'{num} is NOT a prime number.')
    else:
        print(f'{num} is a prime number.')

    restart = input('Would you like to Restart? y/n\n')
    if restart.lower() != 'y':
        break
