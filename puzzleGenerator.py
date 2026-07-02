import random

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

Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #list of letters to fill empty spaces on the grid

def generatePuzzleGrid(words):
     rows, cols = 15, 15
     grid = [[' ' for _ in range(cols)] for _ in range(rows)]
     
     for word in words:
          placed = False
          while (not placed):
               row = random.randint(0, 14) # I generate a random row value from index 0 to 14
               col = random.randint(0, 14) # I generate a random column value from index 0 to 14
               dr, dc = random.choice(Directions) # I generate a random direction value as (dr, dc) from the list Directions
               for letter in range(len(word)): #I loop through every letter in the word from the words list in the GUI file (or a temporary testing list in this file)
                    currentRow = row + (letter * dr)
                    currentColumn = col + (letter * dc)
                    if 0 <= currentRow < 15 and 0 <= currentColumn < 15:  #to avoid index errors
                         if grid[currentRow][currentColumn] == ' ': # checking if the grid is empty
                              grid[currentRow][currentColumn] = word[letter] # filling up the randomised chosen space with the letter from the word
                              placed =  True # telling the loop that it is finished                          
          
          for r in range(15):
               for c in range(15):
                    if grid[r][c] == ' ':
                         grid[r][c] = random.choice(Letters)