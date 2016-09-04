anoi=int(input("entre com o ano:"))
salario=int(input("entre com seu salario:"))
anof=int(input("entre com o ano:"))
ajuste=0.015
anoi=anoi+1
i=1
while anoi<=anof:
    if anoi<=1995 or i==1:
        ajuste=ajuste
    else:
        ajuste=ajuste*2
    salario=salario+salario*ajuste 
    print (anoi,"o ajuste foi de:",ajuste*100,"% , salario com ajuste de R$",salario)
    anoi=anoi+1
    i=i+1
