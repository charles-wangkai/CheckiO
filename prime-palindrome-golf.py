def golf(n):
 while 1:
	n+=1;s=str(n)
	if(s==s[::-1])&all(n%i for i in range(2,n)):return n