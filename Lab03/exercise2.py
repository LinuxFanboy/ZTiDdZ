import random
import string

def generate_password():
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(upper_case),
        random.choice(lower_case),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = upper_case + lower_case + digits + special_chars
    password += random.choices(all_chars, k=4)

    random.shuffle(password)

    return ''.join(password)

print(generate_password())

