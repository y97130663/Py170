#!/usr/bin/python

# Script begins
j = 0
k = ['1',2,3]
print('Banana Cake')
for i in range(0,6):
	if i % 2 == 0:
		print('The number is %d' % (i))
	else:
		print('The number is odd')	
print('To print items of a list without loops use this star operator')
print(*k, sep=',')
print(*k, sep='\n')

# Script Ends
