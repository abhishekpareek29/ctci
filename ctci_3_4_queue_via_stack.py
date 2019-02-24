class Stack(object):
  def __init__(self):
    self.items = []

  def push(self, data):
    self.items.append(data)

  def pop(self):
    return self.items.pop()

  def visualize(self):
    print(self.items)

class MyQueue(object):
  def __init__(self):
    self.mainStack = Stack()
    self.tempStack = Stack()

  def push(self, data):
    self.mainStack.push(data)

  def pop(self):
    while self.mainStack.items != []:
      item = self.mainStack.pop()
      self.tempStack.push(item)
    oldest = self.tempStack.pop()
    while self.tempStack.items != []:
      item = self.tempStack.pop()
      self.mainStack.push(item)
    return oldest

  def visualize(self):
    self.mainStack.visualize()


if __name__ == "__main__":
  MyQueue = MyQueue()
  MyQueue.push(11)
  MyQueue.push(12)
  MyQueue.push(13)
  MyQueue.push(14)
  MyQueue.push(15)
  MyQueue.push(16)
  MyQueue.push(17)
  MyQueue.push(18)
  MyQueue.push(19)
  MyQueue.push(20)
  MyQueue.push(21)
  MyQueue.visualize()
  print(MyQueue.pop())
  MyQueue.visualize()
