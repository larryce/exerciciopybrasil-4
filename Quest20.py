qt= int(input("entre com a quantidade de vezes:"))
n= int(input("entre com o numero:"))
fatorial=1
for i in range(qt):
	while(n>1):
		if (n<16):
			fatorial= fatorial*n
			n=n-1
		else:
			print("numero grande")
print("o fatorial é" , fatorial)
