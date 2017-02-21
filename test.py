A = [4,2,9,7,2,3] #Punya Alice
B = [3,2,1,5,6,3] #Punya Bob
c = 0
d = 0
for i in range(len(A)):
	if (A[i]>B[i]):
		c += 1
	elif (A[i]<B[i]):
		d += 1
if c > d :
	print ("Alice Menang")
elif d < c:
	print ("Bob menang")
else:
	print("seri")