n=int(input("entre com o numero:"))
altura= eval(input("entre com a altura:"))
ma=altura
maNumero=n
menorAltura=altura
menorAlturaNumero=n
i=1
while i<3:
    n= int(input("entre com o numero;"))
    altura = input("entre com a altura:")
    if altura>ma:
        ma=altura
        maNumero=n
    if altura<menorAltura:
        menorAltura=altura
        menorAlturaNumero=n
    i=i+1
print ("numero do aluno mais baixo:", menorAlturaNumero, " , ", menorAltura,"metros")
print ("numero do aluno mais alto:", maNumero, " , ", ma,"metros")
