import numpy as np
import re 

# f = open('/home/rapds/Desktop/maptest2.txt', "r")

c=600
l=550

x = np.zeros((l, c),dtype=np.int)

with open('/home/rapds/Desktop/map3.txt','r') as f:
    for line in f:
        if line.startswith('data:'):
        	b = re.findall(r'\d+', line)

w=0;
for i in reversed(xrange(l)):
	for j in xrange(c):
		x[i,j] = b[w]
		w=w+1

print x

# 0 = free space
# 1 = unknown space
# 100 = occupied space
