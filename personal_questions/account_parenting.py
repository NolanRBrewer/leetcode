elements = [
    {"id": 1, "name": "Account 1", "parent": None},
    {"id": 2, "name": "Account 2", "parent": 1},
    {"id": 3, "name": "Account 3", "parent": 1},
    {"id": 4, "name": "Account 4", "parent": 1},
    {"id": 20, "name": "Account 20", "parent": 2},
    {"id": 21, "name": "Account 21", "parent": 2},
    {"id": 31, "name": "Account 31", "parent": 3},
    {"id": 40, "name": "Account 40", "parent": 4},
    {"id": 41, "name": "Account 41", "parent": 4},
]
'''
Given an element, find all the children and ancestors for that element.
1 -> all elements
2 -> [1, 2, 20, 21]
20 -> [1, 2, 20]
direct line: 
return list of elements [most child, all ancestors, AND the root].
[most child, ... , root]
[root, ..., child]

Search for the root: no assumption can be made of root's position. 
'''
'''
Ancestors:
iterate over elements:
    if the element id is the id in question:
        append element to list 
        [4, 1]
        while the element has a parent:
            parent_id = elements parent
            iterate for element with parent id:
                append element to list
                parent_id = elements parent

Children:
    family_stack = []
    children_tree = [41,42]
    while family_stack:
        iterate for account in elements: 
            if element[id] is the parent in an account:
                append account[id] to family stack and children tree
        element = family_stack.pop()
            
return list
'''
'''
test case:
 {"id": 3, "name": "Account 3", "parent": 1}
 family_tree = [3,1, ]
 account: 
'''
def ancestors(elements, element):
    ancestors_tree = []
    ancestors_tree.append(element)
    while element['parent']:
        for account in elements:
            if account['id'] == element['parent']: 
                ancestors_tree.append(account)
                element = account
    return ancestors_tree

def children(elements, element):
    family_stack = [element]
    children_tree = []
    while family_stack:
        element = family_stack.pop()
        for account in elements:
            if account['parent'] == element['id']:
                children_tree.append(account)
                family_stack.append(account)
    return children_tree

def merge_trees(elements, element):
    oldies = ancestors(elements,element) 
    newbies = children(elements,element)
    return oldies + newbies

print(merge_trees(elements, elements[4]))