import random
import string

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

