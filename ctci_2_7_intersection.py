class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def traverse(self):
    next_node = self
    while next_node != None:
      print(next_node.data)
      next_node = next_node.next_node

  def size(self):
    current = self
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count

  def detectintersect(self, d0):
    size_diff = c0.size() - d0.size()
    d_node = d0
    c_node = c0

    # Equilize.
    if size_diff < 0:
      while size_diff < 0:
        d_node = d_node.next_node
        size_diff += 1
    else:
      while size_diff > 0:
        c_node = c_node.next_node
        size_diff -= 1

    # Compare each node.
    while (c_node != None):
      if (c_node == d_node):
        return c_node.data
      c_node = c_node.next_node
      d_node = d_node.next_node
    return False

if __name__ == "__main__":
  c5 = Node(14)
  c4 = Node(12, c5)
  c3 = Node(23, c4)
  c2 = Node(11, c3)
  c1 = Node(14, c2)
  c0 = Node(12, c1)

  d4 = Node(7, c2)
  d3 = Node(3, d4)
  d2 = Node(1, d3)
  d1 = Node(4, d2)
  d0 = Node(2, d1)

  print("========Print LinkedList=========")
  c0.traverse()
  print("========Finish Printing LinkedList=========")
  d0.traverse()
  print("========Intersect=========")
  print(c0.detectintersect(d0))
