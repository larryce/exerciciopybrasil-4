n=int(input("entre com o numero de eleitores:"))
i=0
soma1=0
soma2=0
soma3=0
while i<n:
    voto=int(input("digite 1 para o candidato1, 2 para o candidato2, 3 para o candidato3:"))
    if voto==1:
        soma1= soma1+1
    elif voto==2:
        soma2=soma2+1
    elif voto==3:
        soma3=soma3+1
    i=i + 1
print ("Candidato 1 possui:", soma1, "votos")
print ("Candidato 2 possui:", soma2, "votos")
print ("Candidato 3 possui:", soma3, "votos")
