altura=eval(input("entre com sua altura:"))
peso=eval(input("entre com seu peso:"))
code=eval(input("entre com seu codigo:"))
saida=int(input("entre com 1 para continuar ou 0 para sair:"))
ma=altura
maCode=code
menorAltura=altura
menorAlturaCode=code
maiorPeso=peso
maiorPesoCode=code
menorPeso=peso
menorPesoCode=code
somaAltura=altura
somaPeso=peso
i=0
while saida!=0:
    altura=eval(input("entre com sua altura:"))
    peso=eval(input("entre com seu peso: "))
    code=eval(input("entre com seu codigo:"))
    saida=int(input("entre com 1 para continuar ou 0 para sair:"))
    if altura>ma:
         ma=altura
         maCode=code
    else:
        ma=ma
    if altura<menorAltura:
        menorAltura=altura
        menorAlturaCode=code
    else:
        ma= menorAltura
 
    if peso > maiorPeso:
        maiorPeso = peso
        maiorPesoCode = code
    else:
        maiorPeso = maiorPeso
 
    if peso < menorPeso:
        menorPeso = peso
        menorPesoCode = code    
    else:
        menorPeso = menorPeso
 
    somaAltura = somaAltura + altura
    somaPeso = somaPeso + peso
    i=i+1
if i!=0:
    mediaPeso= eval(somaPeso)/(i+1)
    mediaAltura=eval(somaAltura)/(i+1)
    print(menorPeso,"kg pesa o mais magro, code:",menorPesoCode)
    print(maiorPeso,"kg pesa o mais gordo, code:",maiorPesoCode)
    print(menorAltura,"m mede o mais baixo, code:",menorAlturaCode)
    print(ma,"m mede o mais alto, code:",maCode)
    print(mediaPeso,"kg é a media de peso da academia")
    print(mediaAltura,"m é a media de altura da academia")
