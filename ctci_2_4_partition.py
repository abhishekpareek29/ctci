class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def traverse(self):
    next_node = self
    while next_node != None:
      print(next_node.data)
      next_node = next_node.next_node

  def partition(self, k):
    node = self
    head = node
    while node != None:
      tail = node
      node = node.next_node

    prev = head
    node = head
    while node != None:
      next_node = node.next_node
      if node.data > k:
        tail.next_node = node
        if node != head:
          prev.next_node = node.next_node
        node.next_node = None

      if node.data < k:
        node.next_node = head
        head = node

      node = next_node
      prev = node


if __name__ == "__main__":
  c0 = Node(3)
  c1 = Node(5)
  c2 = Node(8)
  c3 = Node(5)
  c4 = Node(10)
  c5 = Node(2)
  c6 = Node(1)

  c0.next_node = c1
  c1.next_node = c2
  c2.next_node = c3
  c3.next_node = c4
  c4.next_node = c5
  c5.next_node = c6

  c0.traverse()
  print("==============")
  c0.partition(5)
  print("==============")
  c0.traverse()
  print("==============")

