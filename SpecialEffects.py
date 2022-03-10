#!/usr/local/bin/python3

import sys
import math
import time
import subprocess
import argparse


if len(sys.argv) < 2:
    print(f"Utilização: python3 {sys.argv[0]} [[-i Tempo intervalo] PALAVRA1 [PALAVRA2] ]")
    sys.exit(2)

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--float", type=float, default=1.0)
parser.add_argument("palavra", nargs='*' )

args = parser.parse_args()   
tempo=args.float
palavrasRecebidas=args.palavra

print("Efeito 1- Diagonal Esquerda...")

palavra = ' '.join(palavrasRecebidas)

for i, x in enumerate(palavra):
    print(' ' * i + x)
    time.sleep(tempo)


time.sleep(0.2)    
subprocess.run(['clear'])

print("Efeito 2 - Diagonal Esquerda, Palavras Invertidas...")

palavra = ' '.join(palavrasRecebidas)

for i, ch in enumerate(reversed(palavra)):  
    print(' ' * i + ch)  
    time.sleep(tempo)

time.sleep(0.2)    
subprocess.run(['clear'])  

print("Efeito 3 - Diagonais Cruzadas...")

palavra = ' '.join(palavrasRecebidas)

palavra_len = len(palavra) - 1
palavra_half = math.floor(palavra_len/2)

for i, x in enumerate(palavra):
    time.sleep(tempo)
    if(i == palavra_half):
        print(' ' * i, x)
    elif(i < palavra_half):
        print(' ' * i, x, end='')
        print(' ' * (palavra_len - (2 * i + 2)), x)
    else: 
        print(' ' * (palavra_len - i), x, end='')
        print(' ' * (2 * (i - palavra_half) - 2), x)


time.sleep(0.2)    
subprocess.run(['clear'])   

print("Efeito  4 -Diagonal  Direita,  Palavras  por  Ordem Inversa...")

palavra = ' '.join(palavrasRecebidas)
palavra2=palavra.split()
palavra2.reverse()
resultado=' '.join(palavra2)

for i, x in enumerate(resultado):
    print(' ' * (len (resultado) - i) + x)
    time.sleep(tempo)

time.sleep(0.2)    
subprocess.run(['clear'])   

print("Efeito 5  - Texto Deslizante em Ciclo ao Longo da linha...")

palavraInicial = ' '.join(palavrasRecebidas)

indexador = 0
palavra = list(palavraInicial)
lista =  [' '] * 40

for index, letra in enumerate(palavraInicial):
    lista[index] = letra

while(indexador < 40):
    print('|' + lista[indexador], end='')
    time.sleep(tempo)
    if(indexador == 39):
        indexador = 0
        ultimoCaracter = lista[39]
        novaPalavra = [' '] * 40
        for k in range(0, 39):
            novaPalavra[k+1] = lista[k]
        novaPalavra[0] = lista[39]
        lista = novaPalavra 
        print('\n')
    else:
        indexador+=1
       
