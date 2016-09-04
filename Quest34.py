numero = int(input("entre com um numero:"))
i=2
while i<numero:
    if numero%i == 0:
       print("numero não é primo")
    else:
        i = i + 1
        print (numero, "não é primo")
        break
