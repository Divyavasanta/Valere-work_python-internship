n1 = float(input("Enter first number"))
n2 = float(input("Enter second number"))
operator=input("Enter operator : (+,-,*,/,%) ")

if operator == "+":
  print (n1+n2)
elif operator == "-":
  print (n1-n2)
elif operator == "*":
  print(n1*n2)
elif operator == "/":
    if n2 != 0:
         print("n1/n2")
    else:
         print("Error: Division by zero is not allowed")
elif operator == "%":
    if n2 != 0:
         print("n1%n2")
    else:
        print("Error: Division by Modulo is not allowed")

else:
    print("Invalid Operator")

print("Thank you")






