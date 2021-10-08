def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if char == " ":
            result += " "

        # Encrypt uppercase characters
        elif (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        if char == " ":
            result += " "

        # Encrypt uppercase characters
        elif (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


if __name__ == "__main__":
    text = "Guneet"
    s = 10
    print("Text  : " + text)
    print("Shift : " + str(s))
    print("Encryption: " + encrypt(text, s))
    print("Decryption: " + decrypt(encrypt(text, s), s))
