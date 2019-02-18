class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def kth_last_element(self, k):
    current = self

    # Calculate size of linkedlist.
    size = 0
    while current != None:
      size += 1
      current = current.next_node

    # Get kth last element.
    position = size - k + 1
    current = self
    cur_position = 1
    while cur_position != position:
      cur_position += 1
      current = current.next_node
    return current.data



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

  print(c0.kth_last_element(2))
