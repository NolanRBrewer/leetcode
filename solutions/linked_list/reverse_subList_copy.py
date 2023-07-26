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
    pass