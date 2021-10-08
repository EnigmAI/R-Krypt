lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}


def encrypt(message):
    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            # adds the ciphertext corresponding to the plaintext from the dictionary
            cipher += lookup[letter]
        else:
            # adds space
            cipher += ' '

    return cipher


def decrypt(message):
    decipher = ''
    i = 0

    while True:
        # condition to run decryption till the last set of ciphertext
        if(i < len(message)-4):
            # extracting a set of ciphertext from the message
            substr = message[i:i + 5]
            # checking for space as the first character of the substring
            if(substr[0] != ' '):
                ''' 
                This statement gets us the key(plaintext) using the values(ciphertext) 
                Just the reverse of what we were doing in encrypt function 
                '''
                decipher += list(lookup.keys()
                                 )[list(lookup.values()).index(substr)]
                i += 5  # to get the next set of ciphertext

            else:
                # adds space
                decipher += ' '
                i += 1  # index next to the space

        else:
            break

    return decipher


def main():
    message = "Guneet S Talwar"
    result = encrypt(message.upper())
    print(result)

    message = "AABAAABBABABAABABBBABBAAA"
    result = decrypt(message.lower())
    print(result)


if __name__ == '__main__':
    main()
