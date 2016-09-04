fim=1
while fim!=0:
    soma=0
    i=1
    val= eval(input("entre com o valor ou 0 pra acabar:"))
    while valor>0:
        soma=soma+val
        print ("Produto ",i,": R$ ",val)
        i=i+1
        val= eval(input("entre com o valor ou 0 pra acabar:"))
 
    if soma>0:
        print ("Total:R$", soma)
        formaPag = int(input("entre 1 para cheque ou 2 para dinheiro:"))
        if formaPag==2:
            qtdinheiro= int(input("entre com o valor pago:"))
            troco=qtdinheiro-soma
        else:
            troco=0
        print ("troco em reais:", troco)
        troco=0
    fim=int(input("entre com 0 para sair ou 1 para continuar:"))
