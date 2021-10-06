
adfgvx = 'ADFGVX'


def encrypt(message, keysquare, keyword):
    key = []
    for c in keyword:
        if c not in key:
            key.append(c)
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])
    s = []
    for c in message.lower():
        if c.isalpha() or c.isdigit():
            row, col = divmod(keysquare.index(c), 6)
            s += [adfgvx[row], adfgvx[col]]
    return ''.join(s[j] for i in k for j in range(i, len(s), n))


def decrypt(message, keysquare, keyword):
    key = []
    for c in keyword:
        if c not in key:
            key.append(c)
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])
    m = len(message)
    x = [j for i in k for j in range(i, m, n)]
    y = ['']*m
    for i, c in zip(x, message):
        y[i] = c
    s = []
    for i in range(0, m, 2):
        row, col = y[i:i+2]
        s.append(keysquare[6 * adfgvx.index(row) + adfgvx.index(col)])
    return ''.join(s)


def main():
    print(encrypt('Aditya', 'a9otxj1Iaf0rylsiVItcrdo92daunvzmFAOw', 'Encrypt'))
    print(decrypt('AGGAAFGGAAFA', 'a9otxj1Iaf0rylsiVItcrdo92daunvzmFAOw', 'Encrypt'))


main()
