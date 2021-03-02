
try:
    value = 10/0

except ZeroDivisionError as err:
    print(f"Divide by zero error: {err}")