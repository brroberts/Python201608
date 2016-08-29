class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.prev_node = None
        self.next_node = None


class DoubleLink(object):
    def __init__(self):
        self.tail = None
        self.head = None

    def addNode(self,Node):
        if not self.tail:
            self.tail = Node
            self.head = Node
        elif self.tail is self.head:
            self.tail.next_node = Node
            self.head = Node
            self.head.prev_node = self.tail
        else:
            tmp = self.head
            self.head.next_node = Node
            self.head = Node
            self.head.prev_node = tmp
        return self
    """
    Inserts node at nth position in linked list.
    """
    def insertNode(self, Node, index):
        current = self.getNode(index)
        if current == -1:
            raise ValueError('Index out of bounds')
            # return self
        elif index == 0:
            self.tail.prev_node = Node
            self.tail = Node
            return self
        elif index == self.getSize(): #wont actually get used because getNode() will return -1 for index+2
            print 'wtf'
            self.addNode(Node)
            return self
        else:
            prev_n = current.prev_node
            prev_n.next_node = Node
            current.prev_node = Node
            Node.prev_node = prev_n
            Node.next_node = current
        return self


    def displayList(self):
        arr = []
        current = self.tail
        while current:
            arr.append(current.value)
            current = current.next_node
        print 'this is the list: ', arr

    """
    Returns the size of the linked list.
    """
    def getSize(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next_node
        return count

    """
    Returns the value of the nth node.
    """
    def getValue(self, index):
        current = self.tail
        index = index + 1
        if index > self.getSize():
            return -1
        for i in range(index):
            value =  current.value
            current = current.next_node
        return value

    """
    Returns the nth node.
    """
    def getNode(self, index):
        current = self.tail
        index = index + 1
        if index > self.getSize():
            return -1
        for i in range(index):
            node =  current
            current = current.next_node
        return node

    """
    Removes the nth node from the list.
    """
    def removeNode(self, index):
        node = self.getNode(index)
        if node == -1:
            return -1
        elif index == 0:
            next_n = node.next_node
            next_n.prev_node = None
            self.tail = next_n
            return self
        elif index + 1 == self.getSize():
            prev_n = node.prev_node
            prev_n.next_node = None
            self.head = prev_n
            return self
        else:
            prev_n = node.prev_node
            next_n = node.next_node

            prev_n.next_node = next_n
            next_n.prev_node = prev_n
        return self

#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)

# dlist = DoubleLink()
# dlist.addNode(n1)
# dlist.addNode(n2)
# dlist.addNode(n3)
# dlist.addNode(n4)

# print 'test:', dlist.tail.next_node.next_node.prev_node.value
# dlist.displayList()
# print dlist.getValue(3)
# print dlist.getNode(1).value
# print dlist.removeNode(3).displayList()
# print dlist.insertNode(n5,3).displayList()
