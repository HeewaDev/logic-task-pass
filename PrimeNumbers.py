# Second question
# Take input from user
from typing import Set


set_range = int(input("Specify the prime numbers range : "))

print("\nAll prime numbers range", set_range, "are : ")

for num in range(1, set_range + 1):

    i = 2
    # if the number is not prime pass!
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break

    # If the number is prime then print it.
    if(i != num):
        print(num, end=" ")
