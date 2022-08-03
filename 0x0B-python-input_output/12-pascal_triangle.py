#!/usr/bin/python3
""" Pascal Triangle function
"""


def pascal_triangle(n):
	if n > 0:
		pascal = []
		for i in range(0, n):
			if i == 0:
				pascal.append([1])
			elif i == 1:
				pascal.append([1, 1])
			else:
				tri = [None]*(i+1)
				tri[0], tri[-1] = 1, 1
				for j in range(1, i):
					tri[j] = pascal[-1][j] + pascal[-1][j-1]
				pascal.append(tri)
		return pascal
	return list()
