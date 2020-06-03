import time
# encrypt and decrypt a message using Caesar Cipher
key = 'abcdefghijklmnopqrstuvwxyz'

# Encryption Function
def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""

    #Start timer
    start = time.time()
    result = ''
    
    # Convert all lettes to lowercase
    #Substitute every letter
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    #Stop timer
    end = time.time()

    #Calculate run time
    run = end - start
    print("Encryption took {:.5f} seconds".format(run))
    return result.lower()

# Decryption function
def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    start2 = time.time()
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    end2 = time.time()
    run2 = end2 - start2
    print("Decryption took {:.5f} seconds".format(run2))
    return result

# Taking user input
digits=[]
text = input("Please enter the message you want to encrypt \n")
dob = input("Please enter your DOB in the format MM/DD/YYYY \n")

# Adding digits of DOB to use the sum as offset for encryption
digits.append(dob.split("/"))
offset = 0
for num in digits:
        for i in num:
            i = int(i)
            while(i!=0):
                offset += i % 10
                i = int(i/10)

# Printing both encrypted and decrypted messages
encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)

decrypted = decrypt(offset, encrypted)
print('Decrypted:', decrypted)

# Testing Code

# with open("tests.txt", "r", encoding="utf8") as f:
#     data = f.read()
#     messages = data.split("---")
    
# for i,j in zip(messages, range(3,11)):
#     encrypted = encrypt(j, i)
#     decrypted = decrypt(j, encrypted)
#     print(encrypted)
#     print(decrypted)