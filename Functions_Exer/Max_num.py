# 4. Write a function that takes three parameters of number and determines the largest number among three number
def largest_num(p1,p2,p3):
    return max(p1,p2,p3)

# print(largest_num(5,24,13))
a = int(input("Please provide the first number: "))
b = int(input("Please provide the second number: "))
c = int(input("Please provide the third number: "))

#print(largest_num(p1,p2,p3))


# 5. From question 4, assign the largest number returned to a variable and pass it into the function in question 3 to get the power of 3 of the largest number

lNum = largest_num(a,b,12)

def power_three(value):
     return value ** 3

print(power_three(lNum))






