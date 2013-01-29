#!/usr/bin/python
import sys
from collections import defaultdict

inputfile = open('find_the_mintxt.txt')
data = inputfile.readlines()
Total = (int)(data.pop(0))
l = 1
outputfile = open('find_min_output.txt', 'w')
for i in range(Total):
	line = data[2*i].rstrip()
	line2 = data[2*i+1].rstrip()
	[n, k] = line.split(' ')
	[a, b, c, r] = line2.split(' ')
	n, k, a, b, c, r = int(n), int(k), int(a), int(b), int(c), int(r)	
	if n-k > k+1:
		m = [-1] * (2*k+1)
	else:
		m = [-1] * n
	m[0] = a
	dm = defaultdict(int)	
	dm[a] += 1
	
	for j in range(1, k):
		m[j] = (b *m[j-1] + c) % r
		dm[m[j]] += 1
	wm = n-k if n-k < k+1 else k +1	
	fp = n-1 if n-k < k+1 else (n-k)%(k+1) +k-1
	
	for p in range(wm):	
		if k+p > fp+1: break
		if p >0:
			dm[m[p-1]] = dm[m[p-1]]-1
		d = 0
		while True:
			if dm[d] == 0:
				m[k+p] = d
				dm[d] += 1
				break
			else:
				d += 1
		
	res = m[fp]
	
	print 'Case #%s: %s' % (l, res)
	restr = 'Case #%s: %s\n' if l < Total else 'Case #%s: %s'
	outputfile.write(restr % (l, res))
	l += 1
		
inputfile.close()
outputfile.close()		