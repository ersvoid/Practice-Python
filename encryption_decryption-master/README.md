# encryption_decryption

Each letter of a word or phrase is randomly assinged to:

Uppercase letters

Lowercase letters

Integers 1-26


Functions for:

Encryption of single word

Decryption of single word

Encryption of phrase

Decryption of phrase


Each encryption generates a unique key for the decryption functions to run.


Instructions:

TO ENCRYPT A SINGLE WORD

word = encryption("apple")

print(word) <---this will return [word,key] list

print(word[0]) <---this will return the encrypted word

print(word[1]) <---this will return the key


To DECRYPT A SINGLE WORD

dword = decryption(word[1])

print(dword)


TO ENCRYPT A PHRASE

phrase = auto_encrypt(statement)

print(statement) <----this will return [phrase,key]

print(statement[0]) <---this will return the encrypted phrase

print(statemnt[1]) <---KEY of PHRASE

print(statement[1][0] <---KEY of SINGLE WORD


TO DECRYPT A PHRASE

phrase = auto_decrypt(statement[1])

print(phrase) <---this will return the decrypted phrase
