n= int(input("Enter n value:"))
sum=0
for i in range(1,n):
	if i%3==0 or i%5==0:
		sum=sum+i
print sum		

