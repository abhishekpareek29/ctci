class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.visited = False

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

  def bfs(self):
    queue = Queue()
    queue.push(self)
    self.visited = True

    while not queue.isEmpty():
      node = queue.pop()
      print(node.data)
      node.visited = True

      if node.left != None and node.left.visited == False:
        queue.push(node.left)
      if node.right != None and node.right.visited == False:
        queue.push(node.right)


class Queue(object):
  def __init__(self):
    self.items = []

  def push(self, data):
    self.items.append(data)

  def pop(self):
    return self.items.pop(0)

  def isEmpty(self):
    return self.items == []


if __name__ == "__main__":
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

  t.bfs()
