n=int(input("entre com um numero:"))
print(1)
print(2)
print(3)
teste=5
while teste<n:
    i=2
    v=0
    while i<teste:
        resto=teste%i
        if resto==0:
            i=teste
            v=0
        if resto!=0:
            i=i+1
            v=1
    if v==1:
        print(i)
    teste=teste+1  		
    		
