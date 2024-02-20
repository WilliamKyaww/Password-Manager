import random
import string
import os
import json

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

script_dir = os.path.dirname(os.path.abspath(__file__))

# Save Encryption Key 
key_filename = os.path.join(script_dir, 'key.json')
with open(key_filename, 'w') as key_file:
    json.dump(key, key_file)
    
# Encrypt
def Encryption(original_text):
    ciphered_text = ""
    
    for letter in original_text:
        if letter in chars:  
            index = chars.index(letter)
            ciphered_text += key[index]
        else:
            ciphered_text += letter  
    
    return ciphered_text


# Decrypt
def Decryption(ciphered_text):
    original_text = ""
    
    with open(key_filename, 'r') as key_file:
        key = json.load(key_file)
    
    for letter in ciphered_text:
        if letter in key: 
            index = key.index(letter)
            original_text += chars[index]
        else:
            original_text += letter  
    
    return original_text
    
def Encrypt_File():
    # Read
    filename = os.path.join(script_dir, 'example.txt')
    with open(filename, 'r') as file:
        content = file.read()
        encrypted_text = Encryption(content)

    # Encrypt
    with open(filename, 'w') as file:
        file.write(encrypted_text)

def Decrypt_File():
    # Read 
    filename = os.path.join(script_dir, 'example.txt')
    with open(filename, 'r') as file:
        encrypted_text = file.read()
        decrypted_text = Decryption(encrypted_text)

    # Decrypt
    with open(filename, 'w') as file:
        file.write(decrypted_text)





    
