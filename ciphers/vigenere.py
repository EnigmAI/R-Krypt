ASCII = [c for c in (chr(i) for i in range(32,127))]
def cipher(text, key, decode):
    op = ''
    for i, j in enumerate(text):
        if j not in ASCII:
            op += j
        else:
            text_index = ASCII.index(j)
            k = key[i % len(key)]
            key_index = ASCII.index(k)
            if decode:
                key_index *= -1
            code = ASCII[(text_index + key_index) % len(ASCII)]
            op += code
    return op
def main():
    print(cipher('Aditya', 'Upadhyay', 0))
    print(cipher('vUKYb[', 'Upadhyay', 1))
main()