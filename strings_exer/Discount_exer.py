#5. Write a program that takes the original proce of an item and the discount percentage as inputs (both floats), and calculates the discounted price
price = float(input("Enter the sticker price: "))
discount_percentage = float(input("Enter the percentage discounted: "))

percent = 100

discount = discount_percentage / percent

discounted_price = price - (price * discount)

round_2dec = 2

print("The final price is", round(discounted_price,round_2dec))