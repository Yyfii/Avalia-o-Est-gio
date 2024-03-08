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
def carregar(arq):
     #Carrega e guarda um arquivo JSON em uma variavel
    
    with open(arq) as file:
        dados = json.load(file)
    return dados

#guardar em uma var
fat_por_dia = carregar('dados.json')

#limpar os dados
def clean(fatu):
    new = []
    for dia in fatu:
        if dia['valor'] != 0.0:
            new.append(dia)
    return new

#retornar menor faturamento e seu dia
def menor_fat(fat):
    novo = clean(fat)
    menor = float('inf')
    dia_menor = None
    for dia in novo:
        valor = dia['valor']
        if valor < menor:
            menor = valor
            dia_menor = dia['dia']
    return menor, dia_menor

#retornar maior faturamento e seu dia
def maior_fat(fat):
    novo = clean(fat)
    maior = -float('inf')
    dia_maior = None
    for dia in novo:
        valor = dia['valor']
        if valor > maior:
            maior = valor
            dia_maior = dia['dia']
    return maior, dia_maior

#Numero de dias no mês em que o valor de fatur. diar for superior à media mensal
def media_mensal(fat):
    #media mensal : qtd_vendida(nos utilos 90dias/3meses)
    novo = clean(fat)
    total_fat = sum(dia['valor'] for dia in novo)
    return total_fat/len(novo)

#contar o numero de dias em que o fat dia foi super a media
def count_days(fat):
    md = media_mensal(fat)
    novo = clean(fat)
    count = 0

    for dia in novo:
        if dia['valor'] > md:
            count += 1
    return count

#testes
menor, dia_menor = menor_fat(fat_por_dia)
maior, dia_maior = maior_fat(fat_por_dia)
print("O menor faturamento foi do dia: ",dia_menor,"no valor de: R$ ",menor,"\n")
print("O maior faturamento foi do dia: ",dia_maior,"no valor de: R$ ",maior,"\n")
super_days = count_days(fat_por_dia)
print(" nº dias com faturamento superior a media mensal: ",super_days)

'''


#Questão 4
'''
faturamentos = {"SP":67836.43, "RJ":36678.66, "MG":29165.48,"ES":27165.48, "Outros":19849.53}
sp = float(faturamentos['SP'])
rj = float(faturamentos["RJ"])
mg = float(faturamentos["MG"])
es = float(faturamentos["ES"])
outros = float(faturamentos["Outros"])

def total_faturamento(c1,c2,c3,c4,c5):
    lista = [c1,c2,c3,c4,c5]
    total = sum(lista)
    return total

total_mensal = total_faturamento(sp, rj, mg,es, outros)

def buscar_chave(dict,valor):
    for key,value in dict.items():
        if value == valor:
            return key
    return

def perc_distribuidora(faturou, total):
    per = (faturou * 100)/total
    nome = buscar_chave(faturamentos, faturou)
    print("{} - {:.2f}%".format(nome, per)) 
    return
def per_por_valor(c1,c2,c3,c4,c5):
    lista = [c1,c2,c3,c4,c5]
    for i in lista:
        perc_distribuidora(i, total_mensal)

per_por_valor(sp,rj,mg,es,outros)
'''


#Questão 5
'''
def reverse_string(string):
    new = string[::-1]
    return new 

valor = "maca"
print(reverse_string(valor))

'''