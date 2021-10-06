def encrypt(text):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + 13 - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + 13 - 97) % 26 + 97)

    return result


def decrypt(text):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - 13 - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - 13 - 97) % 26 + 97)

    return result


if __name__ == "__main__":
    text = "Dhruv"
    print("Text  : " + text)
    print("Shift : 13")
    print("Encryption: " + encrypt(text))
    print("Decryption: " + decrypt(encrypt(text).lower()))
