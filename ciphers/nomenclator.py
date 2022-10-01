
import random
import numpy as np
from RNG.LFSR import LFSR
from RNG.FisherYates import fisherYatesShuffle


def createCodeGroups(n,decode=False):
    codegroups = ["{0:03} ".format(i) for i in range(1000)]
   
    
    # Use a LFSR to shuffle the code groups
    L = []
    for ctr,val in enumerate(LFSR(n,[5,6,8,9,11,15,19,31],32)):
        L.append(val)
        if ctr == 1000:
            break
    shuf = fisherYatesShuffle(1000,L)
    codegroups = [codegroups[i] for i in shuf]
    ngrams1 = open('1grams.csv', 'r')
    ngrams2 = open('2grams.csv', 'r')
    ngrams3 = open('3grams.csv', 'r')
    ngrams4 = open('4grams.csv', 'r')
    
    codeDict = {}
    for n,d in enumerate(ngrams1):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
    
    for n,d in enumerate(ngrams2):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
        if n > 50:
            break
    
    for n,d in enumerate(ngrams3):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
        if n > 40:
            break
    
    for n,d in enumerate(ngrams4):
        L = d.split(",")
        codeDict[L[0]] = int(L[1])
        if n > 30:
            break
    normalizingFactor = min(codeDict.values())//3
    for i in codeDict.items():
        codeDict[i[0]] = int(np.ceil(np.sqrt(i[1]//normalizingFactor)))
    codeDict[">"] = 30
    codeDict["_"] = 63
    if decode == False:
        for i in codeDict.items():
            L = []
            for j in range(i[1]):
                L.append(codegroups.pop())
            codeDict[i[0]] = L
        return codeDict
    if decode == True:
        decodeDict = {}
        for i in codeDict.items():
            for j in range(i[1]):
                decodeDict[codegroups.pop()] = i[0]
        return decodeDict
        


def nomenclator(text,key=1,decode=False,usenulls=True,dictionary=False,showgroups=False):
    
    D = createCodeGroups(key,decode)
    if dictionary == True:
        return D

    
    if decode == False:
        codegroups = ["{0:03} ".format(i) for i in range(1000)]
        
        if usenulls == True:

            numNulls = len(text)//25

            for i in range(numNulls):
                r = random.randint(0,len(text))
                text = text[:r] + '_' + text[r:]
                
            for i in range(numNulls//3):
                r = random.randint(0,len(text))
                text = text[:r] + '>' + text[r:]
    
        while "_" in text:
            text = text.replace("_",D["_"][np.random.randint(0,63)],1)
        
        while ">" in text:
            gr = random.choice(codegroups)
            text = text.replace(">",D[">"][np.random.randint(0,30)]+gr,1)
        
        for d in [i for i in D.keys() if len(i) == 4]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)

        for d in [i for i in D.keys() if len(i) == 3]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            
        for d in [i for i in D.keys() if len(i) == 2]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
            
        for d in [i for i in D.keys() if len(i) == 1]:
            T = d.split(",")[0]
            ops = len(D[T]) 
            while T in text:
                text = text.replace(T,D[T][np.random.randint(0,ops)],1)
        
         
        return text
    
    if decode == True:
        X = text.split(" ")
        X.pop()

        for pos,gr in enumerate(X):
            X[pos] = D[gr+" "]

        if showgroups == True:
            return X

        while ">" in X:
            pos = X.index(">")
            X[pos:pos+2] = ""

        while "_" in X:
            pos = X.index("_")
            X[pos] = ""

            
        return "".join(X)


def nomenclatorExample():
    
    from Ciphers.UtilityFunctions import preptext

    print("Example of the Nomenclator Cipher")

    textfile = open('Text.txt','r')
    ptext = preptext(textfile.readline(),silent=True)
    ptext = ptext[:200]
    
    KEY = 3664080377
    
    ctext = nomenclator(ptext,KEY)
    dtext = nomenclator(ctext,KEY,decode=True)
    
    print("Plaintext is:\n{}\n\n".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))

    print("\n\nDoes the Text Decode Correctly?",dtext == ptext)

def PrintCodes(n,decode=False):
    
    D = createCodeGroups(n,decode=decode)
    
    if decode == False:
        for i,j in sorted(D.items()):
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and len(i) == 1:
                S = i + ": "
                for ctr,grp in enumerate(j,1):
                    S += grp
                    if ctr % 7 == 0 and grp != j[-1]:
                        S += "\n   "
                yield S
    
        for L in [2,3,4]:
            for i,j in sorted(D.items()):
                if len(i) == L:
                    S = i + ": "
                    for ctr,grp in enumerate(j,1):
                        S += grp
                        if ctr % 7 == 0 and grp != j[-1]:
                            S += "\n   " + " "*(L-1)
                    yield S
    
        S = "_: "
        for ctr,grp in enumerate(D["_"],1):
            S += grp
            if ctr % 7 == 0 and grp != j[-1]:
                S += "\n   "
        yield S
        
        S = ">: "
        for ctr,grp in enumerate(D[">"],1):
            S += grp
            if ctr % 7 == 0 and grp != j[-1]:
                S += "\n   "
        yield S
        
    if decode == True:
        ctr = 0
        S = ""
        for i,j in sorted(D.items()):
            if ctr % 3 == 0 and ctr != 0:    
                yield S
                S = ""
            S += "{}{:<4}  ".format(i,j)
            ctr += 1

#nomenclatorExample()
#for i in PrintCodes(1,decode=True):
#    print(i)