from cryptography.fernet import Fernet

# Generate and save an encryption key
key = Fernet.generate_key()
with open("ransom_key.key", "wb") as key_file:
    key_file.write(key)

print("🔑 Encryption key generated and saved as 'ransom_key.key'.")
