'''
Given an m x n grid of characters board and a string word, return true if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: word="ABCCED", board:

    { 'A', 'B', 'C', 'E' },
    { 'S', 'F', 'C', 'S' },
    { 'A', 'D', 'E', 'E' }
'''
def dfs(board, word, i, j, k):
    if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
        return False 
    
    if k == len(word) - 1:
        return True
    
    tmp, board[i][j] = board[i][j], '/'

    res = dfs(board, word, i-1, j, k+1) or \
          dfs(board, word, i+1, j, k+1) or \
          dfs(board, word, i, j-1, k+1) or \
          dfs(board, word, i, j+1, k+1) 

    board[i][j] = tmp
    return res

       

def exist(board, word):
    for i in range(len(board)):
       for j in range(len(board[0])):
          if dfs(board, word, i, j, 0):
             return True
    return False
       

def main():
  # Test Case 1
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "ABCCED"
  print(exist(board, word)) # expected output: True

  # Test Case 2
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "SEE"
  print(exist(board, word)) # expected output: True

  # Test Case 3
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "ABCB"
  print(exist(board, word)) # expected output: False

  # Test Case 4
  board = [['a','a']]
  word = "aaa"
  print(exist(board, word)) # expected output: False

  # Test Case 5
  board = [['a']]
  word = "a"
  print(exist(board, word)) # expected output: True

  # Test Case 6
  board = [
      ['a','b','c','d','e'],
      ['f','g','h','i','j'],
      ['k','l','m','n','o'],
      ['p','q','r','s','t'],
      ['u','v','w','x','y'],
      ['z','a','b','c','d']
  ]
  word = "abcde"
  print(exist(board, word)) # expected output: True

  # Test Case 7
  board = [
      ['a','b','c','d','e'],
      ['f','g','h','i','j'],
      ['k','l','m','n','o'],
      ['p','q','r','s','t'],
      ['u','v','w','x','y'],
      ['z','a','b','c','d']
  ]
  word = "zabcd"
  print(exist(board, word)) # expected output: True

main()
