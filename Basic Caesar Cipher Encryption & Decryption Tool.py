def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    print("🔐 Caesar Cipher Encryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift number (e.g. 3): "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("🔒 Encrypted Message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("🔓 Decrypted Message:", decrypted)
    else:
        print("❌ Invalid option. Choose E or D.")
