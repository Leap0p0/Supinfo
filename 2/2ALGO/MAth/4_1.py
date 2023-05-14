def cout_minimal_planter_dyn_top_down(matrice):
    #DEF
    memo = {} # stocker les résultats des sous-problème 
    def planter(i, j, memo):
        if (i, j) in memo: # déjà stocké ?
            return memo[(i, j)]
        if i == 0:
            return 0
        res = float('inf')
        for k in range():
            if k != j:
                res = min(res, planter(i-1, k, memo))
        memo[(i, j)] = res + matrice[i-1][j]
        return memo[(i, j)]
    
    res = float('inf')

    for j in range(len(matrice[0])):
        res = min(res, planter(len(matrice), j, memo))
    return res

# Récupérer la matrice depuis le fichier
def lire_matrice_depuis_fichier(nom_fichier):
    matrice = []
    with open(nom_fichier, 'r') as f:
        for line in f:
            matrice.append(list(map(int, line.strip().split())))
    return matrice

matrice = lire_matrice_depuis_fichier('tree.txt')
resultat = cout_minimal_planter_dyn_top_down(matrice)
print("Matrice :", matrice)
print("Coût minimal de la plantation :", resultat)