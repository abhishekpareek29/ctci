class Stack(object):
  def __init__(self):
    self.items = []
    self.at = [self.items]

  def push(self, data):
    if len(self.at[-1]) >= 3:
      self.at.append([])
      self.at[-1].append(data)
    else:
      self.at[-1].append(data)

  def pop(self):
    node = self.at[-1].pop()
    if len(self.at[-1]) == 0:
      self.at.pop()
    return node

  def popAt(self, at):
    node = self.at[at].pop()
    if len(self.at[at]) == 0:
      self.at.pop(at)
    return node

  def visualize(self):
    print(self.at)

class SetOfStacks(object):
  def __init__(self):
    self.Stack = Stack()

  def push(self, data):
    self.Stack.push(data)

  def pop(self):
    return self.Stack.pop()

  def popAt(self, at):
    return self.Stack.popAt(at)

  def visualize(self):
    return self.Stack.visualize()

if __name__ == "__main__":
  mySetOfstack = SetOfStacks()
  mySetOfstack.push(11)
  mySetOfstack.push(12)
  mySetOfstack.push(13)
  mySetOfstack.push(14)
  mySetOfstack.push(15)
  mySetOfstack.push(16)
  mySetOfstack.push(17)
  mySetOfstack.push(18)
  mySetOfstack.push(19)
  mySetOfstack.push(20)
  mySetOfstack.push(21)

  print("=====Min of Stack======")
  mySetOfstack.visualize()
  print(mySetOfstack.pop())
  print(mySetOfstack.popAt(2))
  mySetOfstack.visualize()
  print(mySetOfstack.pop())
  mySetOfstack.visualize()
  print(mySetOfstack.pop())
  mySetOfstack.visualize()
