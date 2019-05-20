

"""Un algorithme extrêmement simple pour résoudre votre mission est :

    Si votre vitesse verticale est égale ou inférieure à -40 (donc la capsule chute plus vite que 40m/s), 
		alors il faut ralentir : vous indiquez donc une poussée des gaz à 4 pour inverser la tendance et ralentir la chute.
    Si la vitesse verticale est supérieure à -40 (la capsule chute à une vitesse modérée, acceptable pour l'atterrissage), 
		vous laissez la capsule chuter : vous indiquez une poussée des gaz à 0.
	poussée des gaz ::: power ente 0 et 4 	

"""
# Pour atterrir en toute securite, notre vitesse de chutte (v_speed) doit etre plus petite que 40
# Si on monte, la valeur de v_speed est positif
# La vitesse des propulseur est comprise entre 0 et 4 qui veut dire entre 0 et 4m/s
# la vitesse de la chutte si les propulseurs sont eteints est de 3,711m/s
	


# Exemple 1 -----------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # v_speed: the vertical speed (in m/s), can be negative.
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

	
	"""
		Résolution exemple 1:
	"""
    # Vu que l'objet est en chutte libre, il n'avance pas mais recule
    # Sa vitesse verticale est du coup negative
    # On doit rester a une vitesse de chutte inferieure a -40
    # Donc tant que notre vitesse est superieure, inutile d'utiliser les propulseurs
    if v_speed > -40 : # on pourrait garder une marge de securite en mettant la valeur 38 plutot que 40
        # On envoit 2 entier
        # le 1er est l'inclinaison qu'on laisse a 0
        # Le second c'est la vitesse des propulseurs
        print ("0 0")
    
    else :
        print ("0 4")
    






# Exemple 2 -----------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # v_speed: the vertical speed (in m/s), can be negative.
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
	
	"""
		Résolution exemple 2:
	"""
    # Vu que l'objet est en chutte libre, il n'avance pas mais recule
    # Sa vitesse verticale est du coup negative
    # On doit rester a une vitesse de chutte inferieure a -40
    # Donc tant que notre vitesse est superieure, inutile d'utiliser les propulseurs
    if v_speed > -40: # on pourrait garder une marge de securite en mettant la valeur 38 plutot que 40
        speed=0
    else:
        speed=4

    # On envoit 2 entier
    # le 1er est l'inclinaison qu'on laisse a 0
    # Le second c'est la vitesse des propulseurs
	print("0",speed)