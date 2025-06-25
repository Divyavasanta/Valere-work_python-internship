try:
    result = 50 / 10
    print("Your answer is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# with exception:

try:
    result = 40 / 0

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# with exceptionn e:

try:
    result = 40 // 0
    print("Your answer is:", result)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    print("Exception details:", e)

# else clause:

try:
    res = 50 / 25
    print("Your answer is:", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No exceptions occurred, result is:", res)

# finally clause:

try:
    res = 50 // 0
    print(res)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("No exceptions occurred, result is:", res)

finally:
    print("This block always executes, regardless of exceptions.")
