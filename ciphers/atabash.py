def atbash(text):
    # encrypt + decrypt
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr(90 - ord(char) + 65)

        # Encrypt lowercase characters
        else:
            result += chr(122 - ord(char) + 97)

    return result


def main():
    # encrypting
    message = 'dhruv'
    print(atbash(message))

    # decrypting
    message = 'WSIFE'
    print(atbash(message))


if __name__ == '__main__':
    main()
