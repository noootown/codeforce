# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# http://bit.ly/2IoWPwu
# https://wiki.python.org/moin/TimeComplexity
# http://mropengate.blogspot.com/2015/06/algorithm-amortized-analysis.html

import random

class RandomizedSet(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.nums, self.pos = [], {}

  def insert(self, val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.pos:
      self.nums.append(val)
      self.pos[val] = len(self.nums) - 1
      return True
    return False

  def remove(self, val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val in self.pos:
      idx, last = self.pos[val], self.nums[-1]
      self.nums[idx], self.pos[last] = last, idx
      self.nums.pop();
      self.pos.pop(val, 0)
      return True
    return False

  def getRandom(self):
    """
    Get a random element from the set.
    :rtype: int
    """
    return self.nums[random.randint(0, len(self.nums) - 1)]


    # Your RandomizedSet object will be instantiated and called as such:
    # obj = RandomizedSet()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()