# This program tells you if a number is odd or even

number = int(input("What number would you like to check? "))
check = number % 2

if check > 0:
    print("This is an odd number: " + str(check))
else:
    print("This is an even number: " + str(check))
