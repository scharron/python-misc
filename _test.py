import _list
import unittest

class Test_list(unittest.TestCase):
  def setUp(self):
    self.list1 = [1, 2, 3, 4, 5]
    self.list2 = [[1], [2, 3], [4, 5]]
    self.list3 = [1, [2], [[3, 4], [5]]]

  def test_flatten(self):
    self.assertTrue(_list.flatten(self.list2) == self.list1)
    self.assertTrue(_list.flatten(self.list2, True) == self.list1)
    self.assertTrue(_list.flatten(self.list3, True) == self.list1)

if __name__ == '__main__':
  unittest.main()
