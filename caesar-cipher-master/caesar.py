abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lst = []
new_lst = []
dlst = []
dnew_lst = []


def caesar_encrypt():
    word = input("Please enter a word: ").lower()
    for w in word:
        lst.append(w)
    choice = input("Please choose a key from 1 to 26: ")
    new_word = ""
    for l in lst:
        index = abc.index(l) + int(choice)
        if index > 25:
            index -= 25
        new_letter = abc[index]
        new_lst.append(new_letter)
        new_word = "".join(new_lst)
    print("Your encrypted word is " + new_word.capitalize())


def caesar_decrypt():
    dword = input("Please enter a word: ").lower()
    for w in dword:
        dlst.append(w)
    dchoice = input("Please enter your key: ")
    dnew_word = ""
    for l in dlst:
        dindex = abc.index(l) - int(dchoice)
        if dindex < 0:
            dindex += 25
        dnew_letter = abc[dindex]
        dnew_lst.append(dnew_letter)
        dnew_word = "".join(dnew_lst)
    print("Your decrypted word is " + dnew_word.capitalize())

caesar_encrypt()
caesar_decrypt()