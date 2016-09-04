n=int(input("entre com o numero de idades:"))
i=0
soma=0
while i<n:
    idade= int(input("entre com a idade:"))
    soma=soma + idade
    i=i+1
media=soma/i
print ("media igual a", media)
if media<=25:
    print("turma jovem")
elif 25<media<=60:
    print("turma adulta")
else media>60:
    print("turma idosa")
