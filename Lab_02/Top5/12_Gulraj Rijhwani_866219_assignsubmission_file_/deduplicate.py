#!/usr/bin/env python3
"""
Highlight duplicates in an arbitrary file of string values
"""
import time

class TreeNode:

# Instantiate self - with value if supplied
# -- None value used for initial node at the root of the tree
#   def __init__(self, value=None):
#     self.__id = value
  def __init__(self):
    self.__id = None
    self.__leftNode = None
    self.__rightNode = None

# CheckID locates the position of the value in the tree and then:
# -- if matched returns false as a duplicate
# -- otherwise instantiates the next node in the tree
  def checkID(self, value):
    # print("checking {!s:s}".format(value))
    # if currently unsassigned assign directly and assume correct
    if self.__id == None:
      self.__id = value
      # print("directly assigned ({!s:s})".format(self.__id))
      return True

    else:
      # print("node value: {!s:s}".format(self.__id))
      # if value matched return - we have a duplicate
      if self.__id == value:
        # print("duplicate")
        return False

      # if test value less than current we traverse left
      elif value<self.__id:
        # print("check less")
        # if there is no current left node create it
        if self.__leftNode == None:
          self.__leftNode = TreeNode()
        # delegate the result checking to the next node down
        return self.__leftNode.checkID(value)

      # if test value less than current we traverse right
      else:
        # print("check more")
        # if there is no current right node create it
        if self.__rightNode == None:
          self.__rightNode = TreeNode()
        # delegate the result checking to the next node down
        return self.__rightNode.checkID(value)


if __name__ == "__main__":
    
  root = TreeNode()
  start_time = time.time()
  with open('lucky_ids4.txt','r') as luckyfile:
    for l in luckyfile:
      v = l.rstrip('\n')
      if not root.checkID(v):
        print("{!s:s} is a duplicate".format(v))

end_time = time.time()

print("\nRunning time: ", end_time-start_time)