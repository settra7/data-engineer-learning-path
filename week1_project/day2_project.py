while True:
    x = input('Enter your age: ')
    if not x.isdigit():
        print("Please enter a valid age.")
        continue
    x = int(x)
    if x <= 0 or x > 120:
        print("Please enter a valid age.")
        continue
    if x < 18:
        print("Access Restricted.")
    elif x >= 18 and x <= 59:
        print("Welcome!")
    else:
        print("Discount for pensioners.")
    break