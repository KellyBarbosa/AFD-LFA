estados = input().split(" ")
simbolos = input().split(" ")
nTransicoes = int(input())
afd = {}

for i in estados:
    afd[i] = {}

for i in range(0,nTransicoes):
    o, c, d = input().split(" ")
    if c not in afd[o]:
        afd[o][c] = d

estadoInicial = input()
estadosFinais = input().split(" ")
palavras = input().split(" ")

for palavra in palavras:
    estadoAtual = estadoInicial
    erro = 0
    for letra in palavra:
        try:
            estadoAtual = afd[estadoAtual][letra]
        except KeyError:
            erro = 1
            break
    if (estadoAtual not in estadosFinais) or (erro == 1):
        print('N')
    else:
        print('S')