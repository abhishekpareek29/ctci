class Node(object):

    def __init__(self, data=None, next_node=None):
      self.data = data
      self.next_node = next_node

    def traverser(self):
      next_node = self
      while next_node != None:
        print(next_node.data)
        next_node = next_node.next_node

    def rmv_dup_n1(self):
      prev = self
      # memo = set(prev.data)
      memo = {prev.data}
      current = prev.next_node
      while current != None:
        data = current.data
        if data in memo:
          prev.next_node = current.next_node
        else:
          memo.add(data)
        prev = current
        current = current.next_node

    def rmv_dup_n2(self):
      current = self
      while current != None:
        pointer = current
        data = pointer.data
        while current != None:
          prev_node = current
          next_node = current.next_node

          if next_node != None:
            if next_node.data == data:
              prev_node.next_node = next_node.next_node

          current = next_node
        current = pointer.next_node

c0 = Node(12)
c1 = Node(14)
c2 = Node(12)
c3 = Node(23)
c4 = Node(12)
c5 = Node(14)

c0.next_node = c1
c1.next_node = c2
c2.next_node = c3
c3.next_node = c4
c4.next_node = c5

print("============Original linkedlist============")
c0.traverser()
# c0.rmv_dup_n2()
c0.rmv_dup_n1()
print("======After duplicates are removed=========")
c0.traverser()

