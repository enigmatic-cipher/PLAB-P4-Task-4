"""
Given n as input. Print following pattern using For loop.
n=5
5 
54 
543 
5432 
54321
"""

n = 5
pt = ""
for i in range (n, 0, -1):
  pt = pt + str(i)
  print(pt)
