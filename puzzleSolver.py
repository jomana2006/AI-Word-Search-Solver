import time

Directions = [
     (0 , 1), #right direction
     (0 , -1), #left direction
     (1 , 0), #down direction
     (-1 , 0), #up direction
     (1 , 1), #down-right diagonal direction
     (-1 , -1), #up-left diagonal direction
     (1 , -1), #down-left diagonal direction
     (-1 , 1) #up-right diagonal direction
]

def typeWriter(text, delay=0.03):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()
    
def findWordInDirection(grid, word, letter, row, col, dr, dc):
     if letter == len(word):
          return True
     currentRow = row + (letter * dr)
     currentColumn = col + (letter * dc)
     if 0 <= currentRow < 15 and 0 <= currentColumn < 15:
          if grid[currentRow][currentColumn] != word[letter]:
               return False
          else:
               return findWordInDirection(grid, word, letter+1, row, col, dr, dc) #recursion, moving onto next index
     return False
    
def solvePuzzleGrid(grid, words):
     ans = [] #list that holds solutions
     
     for word in words: 
          found = False
          
          typeWriter(f"Searching for {word}...")
          
          for row in range(15):
               if found:
                    break
               for col in range(15):
                    if found:
                         break
                    
                    for dr, dc in Directions:
                         if grid[row][col] == word[0]: #checks if current cell has the first letter of the word
                              if findWordInDirection(grid, word, 0, row, col, dr, dc): #find the first letter in the given direction
                                             typeWriter(f"Appending {word} at row {row}, col {col}")
                                             ans.append((word, row, col, dr, dc))
                                             found = True
                                             break
          typeWriter(f"{word} found!")
     
     return ans

# temporary testing

if __name__ == "__main__":
    from puzzleGenerator import generatePuzzleGrid
    words = ["CAT", "DOG", "BIRD", "LION", "TIGER"]
    grid = generatePuzzleGrid(words)
    for row in grid:
        print(" ".join(row))
    print("----------")
    results = solvePuzzleGrid(grid, words)
    for word, row, col, dr, dc in results:
         print(f"{word} found at row {row}, col {col}, direction ({dr},{dc})")