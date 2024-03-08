import json
import pandas as pd

#Questão 1 
'''
Resposta = 91
'''

#Questão 2
'''
def Fibonacci(valor):
    seq = [0, 1, 1, 2]
    num = 0
    if valor >= 2:
        while seq[-1] < valor:
            num = seq[-1] + seq[-2]
            seq.append(num)
            if(valor in seq):
                print(valor, " está presente na sequência: ", seq)
        print(valor, "não está na sequência: ",seq)
        return seq
        
    else:
        if valor in seq:
            print(valor, " está na sequência: ",seq)
        else:
            print(valor, "não está na sequência: ",seq)

Fibonacci(100)

'''

#Questão 3


'''
#ler arquivo
with open('dados.json') as file:
    dados = json.load(file)
    #pegar a chave
    for dado in dados:
        dia = dado["dia"]
        valor = dado["valor"]
        print(f"Dia: {dia}, Valor:{valor}")
        if valor == 0.0:
            print("oi")

#tratar dados
#menor valor, chave e valor
#maior valor, chave e valor
#calcular media mensal
#dia de faturamento superior a media mensal


'''

#Questão 4

faturamentos = {"SP":66836.43, "RJ":36678.66, "MG":27165.48, "Outros":19849.53}
sp = faturamentos['SP']
rj = faturamentos["RJ"]
mg = faturamentos["MG"]
outros = faturamentos["Outros"]
total = 0

for x in faturamentos:
    for y in faturamentos:
        valores = faturamentos[y]
        total += valores
        print(total)

'''




'''