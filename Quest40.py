codigoc=eval(input("entre com o codigo:"))
Veiculos=int(input("entre com o numero de veiculos:"))
Acidentes= input("entre com o numero de acidentes:")
indiceA=eval((qtyAcidentes)/qtyVeiculos)
maiorIndice=indiceA
maiorIndiceCode=codigoc
menorIndice=indiceA
menorIndiceCode=codigoc
soma=Veiculos
somaVeiculos2000=0
divisorMedia2000=1
if Veiculos<2000:
    somaVeiculos2000=somaVeiculos2000+Acidentes
    divisorMedia2000=divisorMedia2000+1
i = 1
while i<3:
    codigoc= eval(input("entre com o codigo:"))
    Veiculos= int(input("entre com numero de veiculos:"))
    Acidentes= int(input("entre com numero de acidentes:"))
    indiceA=eval((Acidentes)/Veiculos)
    soma=soma+Veiculos
    if indiceA>maiorIndice:
        maiorIndice=indiceA
        maiorIndiceCode=codigoc
    if indiceA<menorIndice:
        menorIndice=indiceA
        menorIndiceCode=codigoc
    if Veiculos<2000:
        somaVeiculos2000=somaVeiculos2000+Acidentes
        divisorMedia2000=divisorMedia2000+1
    i=i+1
print ("menor indice:", menorIndice, " , codigo da cidade:", menorIndiceCode)
print ("maior indice:", maiorIndice, " , codigo da cidade:", maiorIndiceCode)
print ("media de veiculos nas,",i,"cidades = ", eval(soma)/i," veiculos")
print ("media de acidentes em cidades com menos de 2000 veiculos --->",eval(somaVeiculos2000)/divisorMedia2000)
