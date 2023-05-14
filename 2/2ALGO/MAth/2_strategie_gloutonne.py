import numpy as np

def planter_arbres_glouton(T):
    #DEF
    total_cost = 0
    essences = []
    
    for i in range(len(T)):
        essence_min = float('inf') #Le plus grand possible pour le début de la boucle
        essence_min_index = -1
        
        for j in range(len(T[0])):
            if T[i][j] < essence_min:
                # On vérifie que l'essence n'est pas déjà utilisée dans les emplacements contigus
                if i == 0 or j != essences[-1]:
                    essence_min = T[i][j]
                    essence_min_index = j

        total_cost += essence_min # MAJ du cout
        essences.append(essence_min_index)
    
    return total_cost, essences

# Récupérer la matrice depuis le fichier
def lire_matrice_depuis_fichier(nom_fichier):
    matrice = []
    with open(nom_fichier, 'r') as f:
        for line in f:
            matrice.append(list(map(int, line.strip().split())))
    return matrice

    
matrice = lire_matrice_depuis_fichier('tree.txt')
resultat = planter_arbres_glouton(matrice)
print("Matrice :", matrice)
print("Coût total de la plantation :", resultat[0])
print("Essences utilisées :", resultat[1])