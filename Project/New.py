x = int(input("please put an integer: "))
error = str("This number is too small")
nonerror = str("This is a good number")

if x < 0:
    print(error)
else:
    print(nonerror)
