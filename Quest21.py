n=int(input("entre um numero:"))
i=2
while i<n:
    if n%i==0:
        ver=0
        i=n
    else:
        i=i + 1
        ver=1
if ver== 1 or n== 2:
    print (n, "é primo")
else:
    print (n, " nao é primo")
