class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

class LinkedList(object):

  def __init__(self, head=None):
    self.head = head
    self.tail = head

  def insert(self, data):
    prev = self.tail
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      prev.next_node = new_node
      self.tail = new_node
    new_node.next_node = None

  def traverse(self):
    next_node = self.head
    while next_node != None:
      print(next_node.data)
      next_node = next_node.next_node

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count


  def sum_list(self, d):
    c = self
    c_size = c.size()
    d_size = d.size()

    carry = 0
    sum_list = LinkedList()
    c_node = c.head
    d_node = d.head
    for i in range(max(c_size, d_size)):
      if c_node == None or d_node == None:
        if c_node == None:
          sum_amt = 0 + d_node.data + carry
        if d_node == None:
          sum_amt = c_node.data + 0 + carry

        sum_list.insert(sum_amt)
        return sum_list
      else:
        sum_amt = c_node.data + d_node.data + carry
        if sum_amt >= 10:
          sum_amt = sum_amt % 10
          carry = 1
          sum_list.insert(sum_amt)
        else:
          sum_list.insert(sum_amt)
          carry = 0
        c_node = c_node.next_node
        d_node = d_node.next_node

    return sum_list


if __name__ == "__main__":
  c = LinkedList()
  c.insert(7)
  c.insert(1)
  c.insert(6)

  d = LinkedList()
  d.insert(5)
  d.insert(9)
  d.insert(2)

  print("========Print C=========")
  c.traverse()
  print("========Print D=========")
  d.traverse()
  print("========Finish Printing LinkedList=========")
  sum_list = c.sum_list(d)
  print("=======Sum of 2 linkedlists=======")
  sum_list.traverse()

