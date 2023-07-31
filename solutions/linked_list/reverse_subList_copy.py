
'''
Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
reverse the LinkedList from position ‘p’ to ‘q’.
'''

from __future__ import print_function

class Node:

    def __init__(self,value, next= None) -> None:
        self.value = value 
        self.next = next

    def print_list(self):
        temp = self
        while temp != None:
            print(temp.value, end= ' ')
            temp = temp.next
        print()
    
def reverse_sub_list(head, p, q):
    if p == q:
        return head
    
    current = head
    previous = None
    i = 1
    # traverse to a point q
    while current and i < q:
        previous = current
        current = current.next
        i += 1

    last_node_of_first_part = previous

    last_node_of_sub_list = current
    next_node = None 
    i = 0
    while current and i < q - p + 1:
        # traverse the list between q and p while reversing items
        next_node = current.next
        current.next = previous
        previous  = current
        current = next_node
        i += 1

    # join the reversed list back together with the rest of the list
    if last_node_of_first_part:
        last_node_of_first_part.next = previous
    else: 
        head = previous
    
    last_node_of_sub_list.next = current
    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()