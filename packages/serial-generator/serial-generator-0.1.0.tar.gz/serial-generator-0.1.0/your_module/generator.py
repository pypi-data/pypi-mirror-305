import random
import string

def generate_serial(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    serial = ''.join(random.choice(characters) for _ in range(length))
    formatted_serial = '-'.join(serial[i:i+3] for i in range(0, len(serial), 3))
    return formatted_serial
