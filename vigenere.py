from pydoc import plain
from string import ascii_uppercase, ascii_lowercase


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyword=keyword.lower()

    a_chr = {}
    A_chr = {}

    for i in range(len(ascii_lowercase)):        #ключ - номер буквы, значение - буква
        a_chr[i] = ascii_lowercase[i]      

    for i in range(len(ascii_uppercase)):        #ключ - номер буквы, значение - буква
        A_chr[i] = ascii_uppercase[i]  


    i=0
    a_ord = {}
    A_ord = {}
    for c in ascii_lowercase:                   #ключ -буква, значение - номер буквы 
        a_ord[c] = i
        i+=1

    i = 0
    for c in ascii_uppercase:                   #ключ -буква, значение - номер буквы 
        A_ord[c] = i
        i+=1

    if plaintext.islower == True:
        for i in range(len(plaintext)):
            ciphertext += a_chr[ (a_ord[plaintext[i]] + a_ord[keyword[i%len(keyword)]] )%len(ascii_lowercase)]
    else:
        for i in range(len(plaintext)):
            ciphertext += A_chr[ (A_ord[plaintext[i]] + a_ord[keyword[i%len(keyword)]] )%len(ascii_uppercase)]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    keyword=keyword.lower()

    a_chr = {}
    A_chr = {}

    for i in range(len(ascii_lowercase)):        #ключ - номер буквы, значение - буква
        a_chr[i] = ascii_lowercase[i]      

    for i in range(len(ascii_uppercase)):        #ключ - номер буквы, значение - буква
        A_chr[i] = ascii_uppercase[i]  


    i=0
    a_ord = {}
    A_ord = {}
    for c in ascii_lowercase:                   #ключ -буква, значение - номер буквы 
        a_ord[c] = i
        i+=1

    i = 0
    for c in ascii_uppercase:                   #ключ -буква, значение - номер буквы 
        A_ord[c] = i
        i+=1

    if ciphertext.islower == True:
        for i in range(len(ciphertext)):
            plaintext += a_chr[ (a_ord[ciphertext[i]] - a_ord[keyword[i%len(keyword)]] )%len(ascii_lowercase)]
    else:
        for i in range(len(ciphertext)):
            plaintext += A_chr[ (A_ord[ciphertext[i]] - a_ord[keyword[i%len(keyword)]] )%len(ascii_uppercase)]
    return plaintext
