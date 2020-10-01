alpha = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(text, key):
    key = key.lower()
    op = ""
    for i, j in enumerate(text):
        temp = j
        j = j.lower()
        if j == " ":
            op += " "
        else:
            key_a = key[i % len(key)]
            key_a_index = alpha.index(key_a)
            text_a_index = alpha.index(j)
            op_a_index = text_a_index + key_a_index
            op_a = alpha[op_a_index - 26 if op_a_index > 26 else op_a_index]
            if(temp.isupper()):
                op += op_a.upper()
            else:
                op += op_a
    return op

def decode(text, key): 
    key = key.lower()  
    op = ""
    for i, j in enumerate(text):
        temp = j
        j = j.lower()
        if j == " ":
            op += " "
        else:
            key_a = key[i % len(key)]
            key_a_index = alpha.index(key_a)
            text_a_index = alpha.index(j)
            op_a_index = text_a_index - key_a_index
            op_a = alpha[text_a_index + 26 - key_a_index if text_a_index <= key_a_index else text_a_index - key_a_index]
            if(temp.isupper()):
                op += op_a.upper()
            else:    
                op += op_a

    return op
def main():
    print(encode('Aditya', 'upAdhyay'))
    print(decode('Vtjxgz', 'upadHyay'))
main()