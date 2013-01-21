#!/usr/bin/python
from itertools import combinations
#Naive Solution to the Longest Increasing Subsequence Problem
def naive_lis(seq):
	for length in range(len(seq), 0, -1):
		for sub in combinations(seq, length):
			if list(sub) == sorted(sub):
				return sub

seq = [3, 1, 0, 2, 4]
#print naive_lis(seq)

from functools import wraps

def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap
	
@memo
def C(n, k):
	if k == 0: return 1
	if n == 0: return 0
	return C(n-1, k-1) + C(n-1, k)
	
#print C(100, 50)

from collections import defaultdict
n, k = 10, 7
C = defaultdict(int)
for row in range(n+1):
	C[row,0] = 1
	for col in range(1, k+1):
		C[row, col] = C[row-1, col-1] + C[row-1, col]
		
#print C

#Recursive, Memorized DAG Shortest Path
def rec_dag_sp(W, s, t):
	@memo
	def d(u):
		if u == t: return 0
		return min(W[u][v] + d(v) for v in W[u])
	return d(s)
	
def dag_sp(W, s, t):
	d = {u:float('inf') for u in W}
	d[s] = 0
	for u in topsort(W):
		if u == t: break
		for v in W[u]:
			d[v] = min(d[v], d[u] + W[u][v])
	return d[t]
	
def rec_lis(seq):
	@memo
	def L(cur):
		res = 1
		for pre in range(cur):
			if seq[pre] <= seq[cur]:
				res = max(res, 1 + L(pre))
		return res
	return max(L(i) for i in range(len(seq)))
	
def basic_lis(seq):
	L = [1] * len(seq)
	for cur, val in enumerate(seq):
		for pre in range(cur):
			if seq[pre] <= val:
				L[cur] = max(L[cur], 1 + L[pre])
	return max(L)

from bisect import bisect

def lis(seq):
	end = []
	for val in seq:
		idx = bisect(end, val)
		if idx == len(end): end.append(val)
		else: end[idx] = val
	return len(end)
	
#Memorized Recursive Solution to the LCS Problem
def rec_lcs(a,b):
	@memo
	def L(i,j):
		if min(i,j) < 0 : return 0
		if a[i] == b[j]: return 1 + L(i-1, j-1)
		return max(L((i-1),j), L(i,(j-1)))
	return L(len(a)-1, len(b)-1)
	
def lcs(a,b):
	n, m = len(a), len(b)
	pre, cur = [0]*(n+1), [0] *(n+1)
	for j in range(1, m+1):
		pre, cur = cur, pre
		for i in range(1, n+1):
			if a[i-1] == b[j-1]:
				cur[i] = pre[i-1] +1
			else:
				cur[i] = max(pre[i], cur[i-1])
	return cur[n]
	
#Memorized to the Unbonuded Integer Knapsack
def rec_unbounded_knapsack(w, v, c):
	@memo
	def m(r):
		if r == 0 : return 0
		val = m(r-1)
		for i, wi in enumerate(w):
			if wi > r :continue
			val = max(val, v[i] + m(r-wi))
		return val
	return m(c)
	
def unbounded_knapsack(w, v, c):
	m = [0]
	for r in range(1, c+1):
		val = m[r-1]
		for i, wi in enumerate(w):
			if wi > r : continue
			val = max(val, v[i] + m[r-wi])
		m.append(val)
	return m[c]

# 0-1 Knapsack
def rec_knapsack(w, v, c):
	@memo
	def m(k, r):
		if k==0 or r ==0 :return 0
		i = k-1
		drop = m(k-1,r)
		if w[i] > r : return drop
		return max(drop, v[i] + m(k-1, r-w[i]))
	return m(len(w),c)
	
def knapsack(w, v, c):
	n = len(w)
	m = [[0] * (c+1) for i in range(n+1)]
	P = [[False]*(c+1) for i in range(n+1)]
	for k in range(1, n+1):
		i = k-1
		for r in range(1, c+1):
			m[k][r] = drop = m[k-1][r]
			if w[i]>r : continue
			keep = v[i] +m[k-1][r-w[i]]
			m[k][r] = max(drop, keep)
			P[k][r] = keep > drop
	return m, P
	
