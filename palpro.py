n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=n1*n2
n=n3
sum=0
while(n3>0):
	r=n3%10
	sum=(sum*10)+r
	n3=n3/10
if n==sum:
	print "palindrome"
	print sum
else:
	print "not palindrome" 
