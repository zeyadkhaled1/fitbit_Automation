import string
import random

def generate_password(length=10):
    password = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password.append(random.choice(characters))
    return "".join(password)
print(generate_password())
