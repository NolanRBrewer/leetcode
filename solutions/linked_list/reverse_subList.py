'''
Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
reverse the LinkedList from position ‘p’ to ‘q’.

'''

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    # Step 1: Traverse the LinkedList up to the position 'p-1'.
    current = head
    previous = None
    i = 1
    while current and i < p:
        previous = current
        current = current.next
        i += 1

    # Save the node pointing to position 'p-1' to connect it later with the reversed part of the LinkedList.
    last_node_of_first_part = previous

    # Step 2: Traverse the LinkedList from position 'p' to 'q', while reversing it.
    last_node_of_sub_list = current
    next_node = None
    i = 0
    while current and i < q - p + 1:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        i += 1

    # Step 4: Connect the reversed part of the LinkedList with the node saved in step 2.
    if last_node_of_first_part:
        last_node_of_first_part.next = previous
    else:
        head = previous

    # Step 5: If 'p' was greater than 1, connect the node pointing to position 'p-1' with the head of the reversed LinkedList.
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
  result = reverse_sub_list(head, 2, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
