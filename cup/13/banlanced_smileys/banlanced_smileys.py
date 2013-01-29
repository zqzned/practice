#!/usr/bin/python
import sys

inputfile = open('balanced_smileystxt.txt')
data = inputfile.readlines()
Total = (int)(data.pop(0))
words = 'abcdefghijklmnopqrstuvwxyz :'
l = 1
outputfile = open('banlanced_smileys_output.txt', 'w')
for line in data:
	valid = True
	line = line.rstrip()
	llen = len(line)
	message = []
	
	pstack = []
	plf = 0
	prf = 0
	for i in range(llen):
		if line[i] in words:
			message.append(line[i])
		elif line[i] == '(':
			if i-1 >=0 and line[i-1] == ':':
				message.append(line[i])
				pstack.append(line[i])
				plf += 1
			else:
				pstack.append(line[i])
		elif line[i] == ')':
			if i-1 >=0 and line[i-1] == ':':
				message.append(line[i])
				pstack.append(line[i])
				prf += 1
			else:
				pstack.append(line[i])
		else:
			valid = False
			break;
	
	if valid == False:
		pass
	else:
		cstack = []
		for j in pstack:
			if j == '(':
				cstack.append(j)
			elif j == ')':
				if len(cstack) > 0:
					cstack.pop()
				elif prf > 0:
					prf -= 1
				else:
					valid = False
					break
		if valid != False:
			if len(cstack) == 0:
				valid = True
			elif len(cstack) <= plf:
				valid = True
			else:
				valid = False
	
	message = 'YES' if valid else 'NO'
	#print 'Case #%s: %s' % (l, message)
	res = 'Case #%s: %s\n' if l < Total else 'Case #%s: %s'
	outputfile.write(res % (l, message))
	l += 1
	
	
inputfile.close()
outputfile.close()			