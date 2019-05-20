import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


## game loop
while True:
    # creer 2 variables, le maximum et notre cible

    cible = []
    #parcourir "range" qui va de 0-7, index commence à 0
    for index in range(8):
        hauteur_mont = int(input())  # represents the height of one mountain.
        print("valeur index.", index, "valeur montagne", hauteur_mont, file=sys.stderr) # Nous indique les valeurs de nos variables (facultatif)
        #comparer la hauteur de la montagne avec max
        cible.append(hauteur_mont)
    # Write an action using print
   

    # The index of the mountain to fire on.
    print(cible.index(max(cible)))
    