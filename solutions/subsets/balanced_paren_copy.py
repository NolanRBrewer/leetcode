from collections import deque


class ParenthesesString:
    def __init__(self,str,openCount, closedCount):
        self.str = str
        self.openCount = openCount
        self.closedCount = closedCount
    
def generate_valid_parentheses(num):
    results = []
    queue = deque()
    queue.append(ParenthesesString('',0,0))
    while queue:
        ps = queue.popleft()
        if ps.openCount == ps.closedCount and ps.openCount == num:
            results.append(ps.str)
        if ps.openCount < num:
            queue.append(ParenthesesString(ps.str + '(', ps.openCount + 1, ps.closedCount))
        if ps.closedCount < ps.openCount:
            queue.append(ParenthesesString(ps.str + ')', ps.openCount, ps.closedCount + 1))
    return results

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
