"""" 1 Questão:  Resposta = 91

indice = 13
soma = 0
k = 0

while  k < indice:
    k = k +1
    soma = soma + k

print(soma)
"""
# Questão 2.
"""
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
"""

# Questão 3.
"""
a) 9 -> n = n + 2
ind = []
i = 1
while i < 10:
    n = i
    i = i + 2
    ind.append(n)
    print(ind)
b) i = i * 2
ind = []
i = 2
while i < 65:
    n = i
    i = i * 2
    ind.append(n)
    print(ind)

c) i = i**2
ind = []
i = 0
while i < 10:
    ind.append(i**2)
    i+=1
print(ind)

d) numpar = numpar ** 2
ind = []
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        ind.append(i**2)
print(ind)
e) 13, 8 + 5, a sequencia soma os dois snumeros anteriores

f) não sei.
"""
# Questão 4.

"""
3 int   -   3 salas 
1 int   -   1 sala

1º Situação:

    # 1ºida:

     #se sala 1 (on) to int1 (on)
     # sala 2 e sala 3- false to int 1
    # int 2 e int 3 - false to sala 1

    # se sala 1 false to int 1
    # sala1 -> int 2 ou int 3
    # int1 -> sala 2 ou sala 3
    

    #2 ida

    # int 2 (on) - sala 3 (off) ->
    # true to sala 2
    # int 2 on - sala 3 on -> 
    # então int 3 - sala 2


    # se sala 1 (on) to int1 (off)
    #int 2 on - sala 3 off ->
    # int 2 -> ou sala 1 ou sala 2
    # int 3 -> 3 salas possiveis
    # int 1 -> sala 2 ou sala 3

"""

# Questão 5
"""
def reverse_string(string):
    new = string[::-1]
    return new 

valor = "maca"
print(reverse_string(valor))

"""

