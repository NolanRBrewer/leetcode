
from __future__ import print_function
class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp != None:
            print(temp.value, end= ' ')
            temp = temp.next
        print()

def reverse(head):
    previous, current, next = None, head, None

    while current != None:
        next = current.next # store the value
        current.next = previous
        previous = current # reverse nodes
        current = next # move to next node

    return previous
    

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()