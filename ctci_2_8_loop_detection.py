class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def detectloop(self):
    current = self
    fast_node = self
    while fast_node != None and fast_node.next_node != None:
      current = current.next_node
      fast_node = fast_node.next_node.next_node
      if current == fast_node:
        current = self
        break
    while current != fast_node:
      fast_node = fast_node.next_node
      current = current.next_node
      if current == fast_node:
        break
    return fast_node.data


if __name__ == "__main__":
  c9 = Node(9)
  c8 = Node(8, c9)
  c7 = Node(7, c8)
  c6 = Node(6, c7)
  c5 = Node(5, c6)
  c4 = Node(4, c5)
  c3 = Node(3, c4)
  c2 = Node(2, c3)
  c1 = Node(1, c2)
  c9.next_node = c2

  print("========Detect Loop in LinkedList=========")
  print(c1.detectloop())
