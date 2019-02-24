class Stack(object):
  def __init__(self):
    self.items = []

  def push(self, data):
    self.items.append(data)

  def pop(self):
    return self.items.pop()

  def visualize(self):
    print(self.items)


if __name__ == "__main__":
  Stack = Stack()
  Stack.push(31)
  Stack.push(12)
  Stack.push(89)
  Stack.push(114)
  Stack.push(15)
  Stack.push(9)
  Stack.push(17)
  Stack.push(18)
  Stack.push(19)
  Stack.push(200)
  Stack.push(21)
  Stack.visualize()

  tempStack = Stack()



