import sys
nLinhas , nWords = 0,0
f = open('poesia.txt','r')
for currLine in f :
    nLinhas = nLinhas + 1
    for currLine in f :
        if currLine.startswith != '\n': # uma linha vazia não tem palavras
            wordsInCurrLine = currLine.split()
            nWords = nWords + len(wordsInCurrLine)
f.close
print (f'O arquivo poesia contém {nWords} palavras')