class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def traverse(self):
    next_node = self
    while next_node != None:
      print(next_node.data)
      next_node = next_node.next_node

  def remove_middle(self):
    current = self
    next_node = current.next_node
    current.data = next_node.data
    current.next_node = next_node.next_node
    return


if __name__ == "__main__":
  c0 = Node(12)
  c1 = Node(14)
  c2 = Node(12)
  c3 = Node(23)
  c4 = Node(51)
  c5 = Node(14)

  c0.next_node = c1
  c1.next_node = c2
  c2.next_node = c3
  c3.next_node = c4
  c4.next_node = c5

  c0.traverse()
  print("==============")
  c4.remove_middle()
  print("==============")
  c0.traverse()

