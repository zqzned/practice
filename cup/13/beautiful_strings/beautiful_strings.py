#!/usr/bin/python
import sys, operator

inputfile = open('beautiful_stringstxt.txt')
data = inputfile.readlines()
Total = (int)(data.pop(0))
words = 'abcdefghijklmnopqrstuvwxyz'
outputfile = open('beautistring_output.txt', 'w')
l = 1
for line in data:
	word = {}
	for c in words:
		word[c] = 0
	line = line.lower()
	for letter in line:
		if letter in words:
			word[letter] += 1
	sorted_items = sorted(word.items(), key=operator.itemgetter(1))
	most_beautiful = 0
	for i in range(1, 27):
		most_beautiful += i * sorted_items[i-1][1]
	#print 'Case #%s: %s' % (l, most_beautiful)
	res = 'Case #%s: %s\n' if l < Total else 'Case #%s: %s'
	outputfile.write(res % (l, most_beautiful))
	l += 1
	
inputfile.close()
outputfile.close()