class CustomError(Exception):
    pass


number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise CustomError("Input number is less than the required number.")
    else:
        print("Eligible to Vote")

except CustomError:
    print("Exception occured: Invalid Age")


# example one more:

class MyCustomError(Exception):
    pass


raise MyCustomError("This is a custom error")
