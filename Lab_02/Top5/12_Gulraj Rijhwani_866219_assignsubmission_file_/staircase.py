#!/usr/bin/env python3
def pStair(n):
  if n<0 or n>20:
    raise Exception
  for k in range(1, n+1):
    print( " " * (n-k) + "#" * k)
    #print(" "*(n+1-k), "#"*k)

if __name__ == '__main__':
  import random
  n = int(random.random()*24-2)
  #n = 4
  print(n)
  pStair(n)
