numero=int(input("entre com o numero:"))
aux=numero
fatorial = 1
print ("fatorial de:", numero)
print (numero,"! = ",)
while aux>0:
    fatorial=fatorial*aux
    if aux>1:
        print(aux, " . ")
    else:
        print(aux)
    aux=aux-1   
print ("=",fatorial)
