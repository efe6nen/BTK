from itertools import product
import string
import os

ch=int(input("1-Easy 2-Normal 3-Hard 4-Extra"))
i=int(input("Min: \n"))
j=int(input("Max: \n"))

if ch==1:
 	p=string.ascii_lowercase+string.ascii_uppercase
elif ch==2:
	p=string.digits
elif ch==3:
	p=string.ascii_lowercase+string.ascii_uppercase+string.digits
elif ch==4:
	p=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file=open("passlist.txt",'w')

for l in range (i,j+1):
	for c in product(p,repeat=l):
		   wrd="".join(c)
		   file.write(wrd)
		   file.write('\n')
size=os.path.getsize("passlist.txt")
print("Done")
