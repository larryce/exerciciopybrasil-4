n= int(input("entre com a quantidade de valores:"))
aux=1
num= int(input("entre com o numero:"))
ma=num
me=num
soma=0
while (aux<=n):
    if (aux<n):
        num= int(input("entre com o numero:"))
    if (num>ma):
        ma=num
    elif(num<me):
        me=num
    soma=soma+num
    aux= aux+1
print("maior numero:", ma)
print("menor numero:" , me)
print("soma igual a :", soma)
