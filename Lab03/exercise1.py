import base64

def base64_encrypt_decrypt():
    choice = input("Do you want to encrypt or decrypt? Type 'E' for encryption or 'D' for decryption: ").upper()
    password = input("Enter the password: ")

    if choice == 'E':
        # Encryption
        password_bytes = password.encode("ascii")
        base64_bytes = base64.b64encode(password_bytes)
        base64_password = base64_bytes.decode("ascii")
        print(f"Encoded password: {base64_password}")
    elif choice == 'D':
        # Decryption
        base64_bytes = password.encode("ascii")
        password_bytes = base64.b64decode(base64_bytes)
        original_password = password_bytes.decode("ascii")
        print(f"Decoded password: {original_password}")
    else:
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")

base64_encrypt_decrypt()
