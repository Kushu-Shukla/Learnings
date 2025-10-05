# Exceptional Handling / Error Handling
# exception = An event that interupts the flow of a program
print("Hello World")

name = 'kushu'
looks = 'n-gorgeous'

if name == 'kushu' and looks == 'gorgeous':
    print('helloo')
elif name == 'kushu' and looks == 'n-gorgeous':
    print('helloo')
else:
    print("tata bye bye")

try:
     result = 10/2
     print(res)
except (ZeroDivisionError, NameError, KeyError, TabError, TypeError, IndexError) as e:
    print(f"Caught an exception: {e}")
    print(result)
finally:
    print("Exection Completed.")

try:
    code = 'n = "hello\nprint(n)'
    exec(code)
except SyntaxError as k:
    print(f"caught an exception: {k}")
finally:
    print("exception completed")
    

#basic exception
try:
    num = int("abc")
    print("Number:", num)
except ValueError:
    print("X Cannot convert string to integer")

#multiple except blocks
try:
    a = 10/0
except ZeroDivisionError:
    print("You divided by zero!")
except ValueError:
    print("Wrong value type")
except Exception as e:
    print("Other error: ",e)

#identifiying all type of execption, use it when we are not able to find the error
try:
    risky_code()
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Exception Completed")

#using eles
try:
    print("No error here")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Runs only if there is no error occurred")

#raising exceptions by ourself
while True:
    num1 = int(input("Please enter a +ve value: "))
    if num1 < 0:
        raise ValueError("Entered value cannnot be zero")
    else:
        break

# making a custom exception 
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong!")
except MyError as e:
    print("Caught custom error:", e)

#nested try....except
try:
    print(2+1)
    try:
        print(20+12)
        x = int("abc")
    except ValueError:
        print("Inner: ValueError")
        raise
except Exception as e:
    print("Outer caught: ",e)