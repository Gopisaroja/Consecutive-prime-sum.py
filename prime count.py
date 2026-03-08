import math
def prime(n):
	primes=0
	for i in range(2,int(math.sqrt(n))):
		if n%i!=0:
			primes=1
		else:
			primes=0
n=int(input("Enter a number:"))
total=0
count=0
for i in range(2,int(math.sqrt(n))):
	if n%i!=0:
		total+=i
		if total>n:
			break
		else:
			total==prime(n)
			count+=1
print(count)
		