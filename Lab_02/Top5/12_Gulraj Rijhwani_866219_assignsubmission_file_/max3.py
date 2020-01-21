#!/usr/bin/env python3
import time

def max3(f):
  setMax3 = set()
  nMin = None
  c = 0
  for l in f:
    l = l.rstrip('\n')
    if c<3 or l>nMin:
      if c>2: setMax3.remove(nMin)
      setMax3.add(l)
      nMin = min(setMax3)
    c += 1
  s = list(setMax3)
  s.sort()
  return tuple(s)

if __name__ == '__main__':
  start_time = time.time()
  with open('lucky_ids2.txt','r') as luckyfile:
    print(max3(luckyfile))
    
end_time = time.time()

print("\nRunning time: ", end_time-start_time)
