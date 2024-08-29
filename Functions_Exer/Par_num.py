# 1. Write a function that takes a number as a parameter and returns True if the number is even

num = int(input("Please provide a number: "))

def even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)

even(num)