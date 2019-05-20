import os
#importe module système d'exploitation 
import random as rd
#importe module pour que l’ordinateur tire aléatoirement un nombre entier.

nombre = rd.randint(0, 10)
print("Jeu du + OU - ? Devine le nombre auquel je pense, entre 1 et 10")
reponse = 0

while reponse != nombre :
  print("Tape un nombre entier entre 0 et 10")
  reponse =int(input())
  if reponse > nombre :
    print ("moins :-( ")
    
  elif reponse < nombre :
    print ("plus :-(D ")
  
else :
  print ("Yes :-) , le nombre =  ", nombre)
  
os.system("pause")
#stoppe le programme et ferme la fenêtre