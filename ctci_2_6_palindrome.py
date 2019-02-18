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

  def insert_head(self, data):
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

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

  def ispalindromepurmutation(self):
    current = self.head
    char_set = set()
    while current != None:
      if current.data in char_set:
        char_set.remove(current.data)
      else:
        char_set.add(current.data)
      current = current.next_node

    if len(char_set) <= 1:
      return True
    else:
      return False

  def ispalindrome(self):
    current = self.head
    reverse_list = LinkedList()
    while current != None:
      reverse_list.insert_head(current.data)
      current = current.next_node

    current = self.head
    last = reverse_list.head
    while current != None:
      if current.data != last.data:
        return False
      else:
        last = last.next_node
      current = current.next_node
    return True

if __name__ == "__main__":
  c = LinkedList()
  c.insert('t')
  c.insert('o')
  c.insert('y')
  c.insert('a')
  c.insert('y')
  c.insert('o')
  c.insert('t')

  print("========Print LinkedList=========")
  c.traverse()
  print("========Finish Printing LinkedList=========")
  ispalindromepurmutation = c.ispalindromepurmutation()
  print(ispalindromepurmutation)
  ispalindrome = c.ispalindrome()
  print(ispalindrome)

