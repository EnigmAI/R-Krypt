import re
map = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 
def map_gen(key):
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    map = [[0] * 5 for row in range(5)]
    key = re.sub(r'[\W]', '', key).upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                map[row][col] = key[0]
                alpha = alpha.replace(key[0], '')
                key = key.replace(key[0], '')
            else:
                map[row][col] = alpha[0]
                alpha = alpha[1:]
    return map

def encrypt(text, key):
    ciphertext = ''
    text = re.sub(r'[\W]', '', text).upper().replace('Q', '')
    R, L  = map_gen(key[0]), map_gen(key[1])

    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        ciphertext += mangle(R, L, digraphs)
    return ciphertext

def mangle(R, L, digraphs):
    a = position(map, digraphs[0])
    b = position(map, digraphs[1])
    return R[a[0]][b[1]] + L[b[0]][a[1]]

def decrypt(text, key):
    ciphertext = ''
    text = re.sub(r'[\W]', '', text).upper().replace('Q', '')
    R, L = map_gen(key[0]), map_gen(key[1])

    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        ciphertext += unmangle(R, L, digraphs)
    return ciphertext.lower()

def unmangle(R, L, digraphs):
    a = position(R, digraphs[0])
    b = position(L, digraphs[1])
    return map[a[0]][b[1]] + map[b[0]][a[1]]

def position(map, ch):
    for row in range(5):
        for col in range(5):
            if map[row][col] == ch:
                return (row, col)
    return (None, None)

def main():
    plaintext = 'Aditya'
    key = ['Upadhyay', 'Encrypt']
    ciphertext = encrypt(plaintext, key)
    print(ciphertext)
    print(decrypt(ciphertext, key))
main()