n= int(input("entre com a quantidade de valores:"))
aux=1
num= int(input("entre com o numero:"))
ma=num
me=num
soma=0
while (num>0 and num<1000):
	while (aux <= n):
            if (aux < n):
	        num = int(input("Digite um número: "))
            if (num > ma):
                ma=num
	    if (num < me):
                me=num
            else:
                print("numeros grandes")
            soma = soma + num
            aux= aux+1
print("maior numero:", ma)
print("menor numero:" , me)
print("soma igual a :", soma)
