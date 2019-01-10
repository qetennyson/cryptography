import string

user_message = input("Enter a message containing only A-Za-z or spaces: ")
user_key = int(input("Enter Caesar encryption key: "))
decrypted = ""

#TODO: ALPHA can be extended to include all possible symbols.
ALPHA = string.ascii_uppercase + string.ascii_lowercase + ' ' + "'"
print(ALPHA)
UPPER_ALPHA = string.ascii_uppercase
print(len(UPPER_ALPHA))
def encrypt(message, key):
    encryption_index = 0
    encrypted = ''
    for letter in message:

        if letter in ALPHA:
            #TODO: Include a try/except here for missing characters in ALPHA.
            encryption_index = ALPHA.index(letter) + key

            if encryption_index >= len(ALPHA):
                encryption_index -= len(ALPHA)
            elif encryption_index < 0:
                encryption_index += len(ALPHA)

            encrypted += ALPHA[encryption_index]

        else:
            print("Not in ALPHA")

    return encrypted

def decrypt(message, key):
    decrypted = ''
    for letter in message:
        decrypted_value = ALPHA.index(letter) - key
        if letter in ALPHA:
            decrypted += ALPHA[decrypted_value]
        else:
            print("Not in ALPHA")
    return decrypted

encrypted_msg = encrypt(user_message,user_key)
decrypted_msg = decrypt(encrypted_msg, user_key)
print(encrypted_msg, decrypted_msg)