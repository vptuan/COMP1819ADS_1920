#!/usr/bin/env python3
def amilucky(f):
  for l in f:
    if l.rstrip('\n') == '001081292':
      return True
  return False

if __name__ == '__main__':
  with open('lucky_ids.txt','r') as luckyfile:
    print(type(luckyfile))
    if amilucky(luckyfile):
      print("I am lucky")
    else:
      print("I am not lucky")

