class Node(object):
  def __init__(self, data):
    self.data = data
    self.adj = []
    self.visited = False

  def insert(self, destination):
    self.adj.append(destination)

  def hasPath(self, destination):
    queue = Queue()
    visited = Queue()
    for i in self.adj:
      queue.push(i)
      visited.push(i)
    self.visited = True

    while not queue.isEmpty():
      node = queue.pop()
      if node.visited == False:
        for j in node.adj:
          queue.push(j)
          visited.push(j)
        node.visited = True

      if visited.contains(destination):
        return True
    return False

class Queue(object):
  def __init__(self):
    self.items = []

  def push(self, data):
    self.items.append(data)

  def pop(self):
    return self.items.pop(0)

  def isEmpty(self):
    return self.items == []

  def contains(self, node):
    if node in self.items:
      return True
    else:
      return False


if __name__ == '__main__':

# 1: [2,3,4,5]
# 2: [3]
# 3: [1]
# 4: [5]
# 5: [2,3]

  g1 = Node(1)
  g2 = Node(2)
  g3 = Node(3)
  g4 = Node(4)
  g5 = Node(5)
  g1.insert(g2)
  g1.insert(g3)
  # g1.insert(g4)
  g1.insert(g5)
  g2.insert(g3)
  g3.insert(g1)
  g4.insert(g5)
  g5.insert(g2)
  g5.insert(g3)

  print(g2.hasPath(g4))
