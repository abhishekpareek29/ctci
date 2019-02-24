class Stack(object):
  def __init__(self):
    self.items = []

  def insert(self, data):
    if len(self.items) != 0:
      top_node = self.items[len(self.items)-1]
      if self.items[top_node.min_index].data > data:
        min_index = len(self.items)
      else:
        min_index = top_node.min_index
    else:
      min_index = 0
    node = Node(data, min_index)
    self.items.append(node)

  def pop(self):
    node = self.items.pop()
    return node.data

  def min(self):
    node = self.items[len(self.items)-1]
    return self.items[node.min_index].data

class Node(object):
  def __init__(self, data=None, min_index=0):
    self.data = data
    self.min_index = min_index

if __name__ == "__main__":
  mystack = Stack()
  mystack.insert(100)
  mystack.insert(29)
  mystack.insert(90)
  mystack.insert(200)
  mystack.insert(12)

  print("=====Min of Stack======")
  print(mystack.min())
