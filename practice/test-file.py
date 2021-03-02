class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, elements=None):
        if elements:
            self.head = Node(elements.pop(0))
            tempnode = self.head
            for i in elements:
                tempnode.next = Node(i)
                tempnode = tempnode.next

    def __repr__(self):
        node = self.head
        temp = []
        while node is not None:
            temp.append(str(node.data))
            node = node.next
        temp.append("None")
        return "->".join(temp)

    def print_ll(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

my_list = LinkedList([1,2,3,4,5,6])
my_list.print_ll()
print(my_list)

