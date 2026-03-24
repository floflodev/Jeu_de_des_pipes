# Version 4
# Objectif : Créer un jeu de dés dans lequel le dés d'un des joueurs a plus de chances de réaliser un petit résultat

import random

# Demande des prénoms
j1 = input("Joueur 1 quel est ton prénom ? ")
j2 = input("Joueur 2 quel est ton prénom ? ")

# Dé truqué pour le joueur 1 
# Les probabilités (weights) correspondent a la valeur située au meme endroit (ex : 1 et 30%)
# Les probabilités sont calculées pour atteindre 100 
des1 = random.choices([1, 2, 3, 4, 5, 6], 
weights=[30, 20, 15, 15, 10, 10])[0]
print(j1, "fait", des1)

# Dé classique pour le joueur 2
des2 = random.randint(1, 6)
print(j2, "fait", des2)

# Comparaison des résultats
if des1 > des2:
    print(j1, "gagne")
elif des1 == des2:
    print("Égalité")
else:
    print(j2, "gagne")
