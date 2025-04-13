from cryptography.fernet import Fernet
import os

# Load the encryption key
def load_key():
    return open("ransom_key.key", "rb").read()

# Decrypt a file and log it
def decrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

    # Log decrypted file
    with open("log.txt", "a") as log_file:
        log_file.write(f"Decrypted: {file_path}\n")

# Decrypt all files in a folder
def decrypt_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' not found.")
        return

    key = load_key()
    fernet = Fernet(key)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name != "README.txt":
            decrypt_file(file_path, fernet)
            print(f"🔓 Decrypted: {file_name}")

# Decrypt test folder
decrypt_folder("ransomware_test")
