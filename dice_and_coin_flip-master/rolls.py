from random import randint as rd

def coin():
    val = rd(1, 3)
    if val == 1:
        print("Heads")
    else:
        print("Tails")
def dfour():
    val = rd(1, 5)
    print("{}".format(val))
def dsix():
    val = rd(1, 7)
    print("{}".format(val))
def deight():
    val = rd(1, 9)
    print("{}".format(val))
def dten():
    val = rd(1, 11)
    print("{}".format(val))
def dtwelv():
    val = rd(1, 13)
    print("{}".format(val))
def dhund():
    val = rd(1, 101)
    print("{}".format(val))
lst = ["1. Coin Flip", "2. d4", "3. d6", "4. d8", "5. d10", "6. d12", "7. d100"]
prob = True
while prob:
    print("Probably Probability")
    print("Please choose an option or q to quit")
    for l in lst:
        print(l)
    choice = input("Take a chance: ")
    if choice == "1":
        coin()
    elif choice == "2":
        dfour()
    elif choice == "3":
        dsix()
    elif choice == "4":
        deight()
    elif choice == "5":
        dten()
    elif choice == "6":
        dtwelv()
    elif choice == "7":
        dhund()
    elif choice == "q":
        break
    else:
        print("Incorrect input")
        continue