try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
finally:
    print("finally")
