num1 = float(input("Enter the first number :"))
operator = input("Enter operator(+,-,*,/):")
num2 = float(input("Enter your second number :"))

if operator == "+":
   print("Result:",num1 + num2)

elif operator == "-":
    print("Result:",num1 - num2)

elif operator == "*":
    print("Result:",num1 * num2)

elif operator == "/":
     print("Result:",num1 / num2 if num2 !=0 else "Error")

else:
  print("Invalid Operator.")


