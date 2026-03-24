# Version 2 
# Objectif : Créer un jeu de dés en désanvantageant un joueur en tronquant son dés pour qu'il ne puisse pas faire plus de 3

# Importe la bibliotheque random pour pouvoir avoir une selection aléatoire
import random 
# Demande le prénom des joueurs
j1 = input("Joueur 1 quel est ton prénom ?")
j2 = input("Joueur 2 quel est ton prénom ?")

#Simule un réel lancé de dés en choissant un nombre aléatoire situés entre 1 et 6
des1 = random.randint(1,6)
# Affiche le resultat
print(j1, "fait", des1)
# Simule un nouveau lancé en bloquant le résultat maximum possible a 3
des2 = random.randint(1,3)
print(j2, "fait", des2)

# Compare les deux lancés et annonce le joueur 1 gagnant si le des1 est superieur a des2 
if des1 > des2 :
    print(j1, "gagne")
# Compare les deux lancés et annonce une égalité si les deux des sont égaux
elif des1 == des2 :
    print("Egalité")
# Annonce le joueur 2 gagnant si les deux conditions précedentes ne sont pas respectées
else : 
    print(j2, "gagne")
