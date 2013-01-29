#!/usr/bin/python
import sys

filehandle = open('alphabet_souptxt.txt')
data = filehandle.readlines()
Total = (int)(data.pop(0))
words = "HACKERUP"
c = 1
output = open('alphabet_soutput', 'a')
for line in data:
	word = {'H':0,'A':0,'C':0,'K':0,'E':0,'R':0,'U':0,'P':0}
	for letter in line:
		if letter in words:
			word[letter] += 1
		if letter == 'C':
			word[letter] -= 0.5
	counter = 0
	
	while True:
		res = True
		for t in word:
			word[t] -= 1
			res = res & (word[t] >= 0)
		if res:
			counter += 1
		else:
			break
	print 'Case #%s: %s' % (c, counter)
	output.write('Case #%s: %s\n' % (c, counter))
	c += 1
	
filehandle.close()
output.close()
				
	
	
