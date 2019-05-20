import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    hauteur_max = 0    
    index_max = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > hauteur_max:
            hauteur_max = mountain_h
            index_max = i

    
            
    # To debug: print("Debug messages...", file=sys.stderr)
    #print("Debug messages...  It should be an integer from 0 to 7", file=sys.stderr)
    # The index of the mountain to fire on.
    print(index_max)