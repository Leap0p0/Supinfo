def cout_plantation_recursive(matrice):
    def cout_plantation_rec(i, j, dernier_arbre):
        if i == len(matrice):
            return 0
        
        cout_min = float('inf')
        for k in range(len(matrice[0])):
            if k != j and k != dernier_arbre:
                cout_min_k = cout_plantation_rec(i + 1, k, j)
                cout_min_k += matrice[i][k]
                if cout_min_k < cout_min:
                    cout_min = cout_min_k

        return cout_min
    
    cout_min = float('inf')

    for j in range(len(matrice[0])):
        cout_min_j = cout_plantation_rec(1, j, -1)
        cout_min_j += matrice[0][j]
        if cout_min_j < cout_min:
            cout_min = cout_min_j
    
    return cout_min

# Récupérer la matrice depuis le fichier
def lire_matrice_depuis_fichier(nom_fichier):
    matrice = []
    with open(nom_fichier, 'r') as f:
        for line in f:
            matrice.append(list(map(int, line.strip().split())))
    return matrice

matrice = lire_matrice_depuis_fichier('tree.txt')
resultat = cout_plantation_recursive(matrice)
print("Matrice :", matrice)
print("Coût minimal de la plantation :", resultat)