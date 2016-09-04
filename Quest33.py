qtNum=eval(input("quantos numeros deseja avaliar?"))
soma=0
i=0
while qtNum>i:
    numero=eval(input("entre com um numero:"))
    if i==0:
        me=numero
        ma=numero
    else:
        if numero>ma:
            ma=numero
        elif numero<me:
            me=numero
    soma=soma+numero   
    i=i+1
    media=soma/numero
print ("a soma dos numeros é:", soma)
print ("o maior numero é:",ma)
print ("o menor numero é:",me)
print ("a media é:",media)
