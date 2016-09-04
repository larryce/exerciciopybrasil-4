n=int(input("entre com um numero:"))
primeTest=5
while primeTest<n:
    i=2
    v=0
    while i<primeTest:
        rest=primeTest%i
        divisao=divisao+1
        if rest==0:
            i=primeTest
            v=0
        if rest!=0:
            i=i + 1
            v=1
    if v==1:
        print (i, "primo\n")
    primeTest=primeTest + 1
print (divisao, "divisões")
