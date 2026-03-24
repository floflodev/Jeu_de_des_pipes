# Version 3 
# Objectif : Créer un jeu de dés dans lequel le dés d'un des joueurs ne pourra tirer que des nombres impairs

# Version 1 avec liste :
# Importe la bibliotheque random
import random 
# Demande le prenom des joueurs
j1 = input("Joueur 1 quel est ton prénom ?")
j2 = input("Joueur 2 quel est ton prénom ?")

# Initialise une liste contenant les 3 nombres impairs situés entre 1 et 6
impairs = [1,3,5]
# Simule un lancés de dés normal et annonce le resultat
des1 = random.randint(1, 6)
print(j1, "fait", des1)
# Simule un lancés de dés, cependant le resultat ne pourra etre selectionnés que dans notre liste d'impairs
des2 = random.choice(impairs)
print(j2, "fait", des2)

# Compare les résultats et annonce le gagnant 
if des1 > des2 :
   print(j1, "gagne")
elif des1 == des2 :
    print("Egalité")
else : 
    print(j2, "gagne")

# Version 2 avec modulo :
# Meme base que la version précédente
import random
j1 = input("Joueur 1 quel est ton prénom ?")
j2 = input("Joueur 2 quel est ton prénom ?")

des1 = random.randint(1, 6)
print(j1, "fait", des1)
# Simule un lancés de dés pour le joueur 2
des2 = random.randint(1, 6)
# Créer une boucle qui relance le dés tant que le nombre est pair
while des2 % 2 == 0:  
    des2 = random.randint(1, 6)
print(j2, "fait", des2)

if des1 > des2:
    print(j1, "gagne")
elif des1 == des2:
    print("Egalité")
else:
    print(j2, "gagne")
