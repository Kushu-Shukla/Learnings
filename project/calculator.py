# num = (int(input("Enter first number: ")))
# num1 = (int(input("Enter second number: ")))
# sum = num + num1
# print("the sum of two numbers are: ",sum)


# subtract = num - num1
# print("the subtraction of two numbers are: ",subtract)

# multi = num * num1
# print("the multiplication of two numbers are",multi)

# divison = num / num1
# print("the divison of two numbers are: ",divison)
# #age subtraction, multi. and division kro

# # good4, ab user driven menu program bnao, jisme tum usse input lo 2 number and then user se pucho uspe kya krna hai like add sub multi and division, and sirf user jo operation bole usi ka output dikhna chahiye
# # sorry need help kitna time lgega call pe?

# # 15 to 30 mins

# tbt

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("""
Menu Item:
      1. Addition
      2. Subtraction
      3. Multiply
      4. Division
      5.logical operator
      6.comparision operator
""")
choice = int(input("Choose the operation from the menu to be performed: "))

if choice == 1:
    sum = num1 + num2
    print(f"Addition of {num1} and {num2}: {sum}")
elif choice == 2:
    sub = num1 - num2
    print(f"subtraction of {num1} and{num2}:{sub}")
elif choice ==3:
    multi = num1 * num2
    print(f"multiplication of { num1} and {num2}: {multi}")
elif choice == 4:
    div = num1 / num2
    print(f"divison of {num1} and {num2}: {div}")
elif choice == 5:
    print("I dont know what to do")
else:
    print("Wrong input")

# airthmetic operators used hogye hai ab, and ab comparison operators use kro and logical operator to upgrade the program
