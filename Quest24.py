n=int(input("entre com o numero de notas:"))
i=0
soma=0
while i<n:
    nota=input("entre com a nota:")
    soma= soma + nota
    i=i + 1
media=soma/i
print ("media igual a: ", media)
