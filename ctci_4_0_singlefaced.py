class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.visited = False
    self.depth = None

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
    # self.visited = True
    self.depth = 1
    faced = []
    faced.append(self)

    while not queue.isEmpty():
      node = queue.pop()
      node.visited = True

      if node.left != None and node.left.visited == False:
        queue.push(node.left)
        node.left.depth = node.depth + 1
        if node.left.depth != faced[len(faced)-1].depth:
          faced.append(node.left)

      if node.right != None and node.right.visited == False:
        queue.push(node.right)
        node.right.depth = node.depth + 1
        if node.right.depth != faced[len(faced)-1].depth:
          faced.append(node.right)

    return faced

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
  t.insert(68)

  faced = t.bfs()
  for node in faced:
    print(node.data)
