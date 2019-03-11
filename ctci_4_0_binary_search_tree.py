class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert(self, data):
    if self.data > data:
      if self.left == None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right == None:
        self.right = Node(data)
      else:
        self.right.insert(data)

  def contains(self, data):
    if self.data == data:
      return True
    elif self.data > data:
      if self.left == None:
        return False
      else:
        return self.left.contains(data)
    else:
      if self.right == None:
        return False
      else:
        return self.right.contains(data)

  def inorder_traverse(self):
    if self.left != None:
      self.left.inorder_traverse()
    print(self.data)
    if self.right != None:
      self.right.inorder_traverse()

  def postorder_traverse(self):
    if self.left != None:
      self.left.postorder_traverse()
    if self.right != None:
      self.right.postorder_traverse()
    print(self.data)

  def preorder_traverse(self):
    print(self.data)
    if self.left != None:
      self.left.preorder_traverse()
    if self.right != None:
      self.right.preorder_traverse()


if __name__ == '__main__':
  t = Node(10)
  t.insert(9)
  t.insert(3)
  t.insert(19)
  t.insert(20)
  t.insert(5)
  t.insert(8)
  t.insert(38)
  t.insert(58)
  t.insert(18)
  t.insert(1)

  # print(t.contains(3))
  t.inorder_traverse()
  print("==================")
  t.postorder_traverse()
  print("==================")
  t.preorder_traverse()


