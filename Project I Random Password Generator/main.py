# code by @tusharkhanna

import string
import random
import pyperclip

def generate_password(length = 8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Password copied to clipboard.")

if __name__ == '__main__':
    length = int(input("Enter the length of the password : "))
    password = generate_password(length)
    print("Generated password:", password)
    copy = input("Do you want to copy the password to the clipboard? (Yes / No) : ").lower().strip()
    if copy == 'yes' or copy == 'y':
        copy_to_clipboard(password)
