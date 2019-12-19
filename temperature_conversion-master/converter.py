units = ["1. Celsius", "2. Fahrenheit", "3. Kelvin"]
c_units = ["1. Fahrenheit", "2. Kelvin"]
f_units = ["1. Celsius", "2. Kelvin"]
k_units = ["1. Celsius", "2. Fahrenheit"]

for unit in units:
    print(unit)
print("\n")
start = input("Please select a starting unit: ")
if start == "1":
    print("You have selected Celsius.")
    val = int(input("Please enter a value: "))
    print("You have input {} degrees C.".format(val))
    for c in c_units:
        print(c)
    convert = input("Please select a conversion unit: ")
    if convert == "1":
        ans = val * 1.8 + 32
        print("{} degrees F".format(ans))
    elif convert == "2":
        ans = val + 273.15
        print("{} degrees K".format(ans))
    else:
        print("Incorrect input. Try again.")
elif start == "2":
    print("You have selected Fahrenheit.")
    val = int(input("Please enter a value: "))
    print("You have input {} degrees fahrenheit.".format(val))
    for f in f_units:
        print(f)
    convert = input("Please select a conversion unit: ")
    if convert == "1":
        ans = (val - 32) / 1.8
        print("{} degrees C".format(ans))
    elif convert == "2":
        ans = (val + 459.67) * (5/9)
        print("{} degrees K".format(ans))
    else:
        print("Incorrect input. Try again.")
elif start == "3":
    print("You have selected Kelvin.")
    val = int(input("Please enter a value: "))
    print("You have input {} degrees Kelvin.".format(val))
    for k in k_units:
        print(k)
    convert = input("Please select a conversion unit: ")
    if convert == "1":
        ans = (val - 32) / 1.8
        print("{} degrees C".format(ans))
    elif convert == "2":
        ans = (val * (9/5)) - 459.67
        print("{} degrees F".format(ans))
    else:
        print("Incorrect input. Try again.")
else:
    print("Incorrect input. Try again.")
