from string import ascii_uppercase, ascii_lowercase

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
   
    shifted_ABC = ascii_uppercase[shift:] + ascii_uppercase[:shift]         #сдвиг
    shifted_abc = ascii_lowercase[shift:] + ascii_lowercase[:shift]        

    d1 = str.maketrans(ascii_uppercase, shifted_ABC)                        #составление словаря для перевода
    d2 = str.maketrans(ascii_lowercase, shifted_abc) 

    d = dict( list(d1.items()) + list(d2.items()) )     #склейка

    ciphertext = plaintext.translate(d)        #перевод
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    shifted_ABC = ascii_uppercase[-shift:] + ascii_uppercase[:-shift]         #сдвиг
    shifted_abc = ascii_lowercase[-shift:] + ascii_lowercase[:-shift]       

    d1 = str.maketrans(ascii_uppercase, shifted_ABC)                        #составление словаря для перевода
    d2 = str.maketrans(ascii_lowercase, shifted_abc) 

    d = dict( list(d1.items()) + list(d2.items()) )     #склейка

    plaintext = ciphertext.translate(d)        #перевод
    return plaintext

print(decrypt_caesar('A'))