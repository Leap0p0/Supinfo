def optimal_planting_cost(matrix):
    #DEF
    n = len(matrix)
    m = len(matrix[0])
    
    # Initialisation de la matrice g
    g = [[float('inf')] * m for _ in range(n)]
    for j in range(m):
        g[0][j] = matrix[0][j]
    
    # Calcul de la matrice g
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                if j != k:
                    g[i][j] = min(g[i][j], g[i-1][k] + matrix[i][j])
    
    # cout min
    min_cost = float('inf')
    for j in range(m):
        min_cost = min(min_cost, g[n-1][j])
    
    # essences utilise
    essences = []
    j = g[n-1].index(min_cost)
    for i in range(n-1, -1, -1):
        essences.append(j+1)
        for k in range(m):
            if k != j and g[i-1][k] + matrix[i][j] == g[i][j]:
                j = k
                break
    
    essences.reverse()
    
    return min_cost, essences

# Récupérer la matrice depuis le fichier
def lire_matrice_depuis_fichier(nom_fichier):
    matrice = []
    with open(nom_fichier, 'r') as f:
        for line in f:
            matrice.append(list(map(int, line.strip().split())))
    return matrice

matrice = lire_matrice_depuis_fichier('tree.txt')
resultat = optimal_planting_cost(matrice)
print("Matrice :", matrice)
print("Coût de la plantation :", resultat[0])
print("Essence [0 à m] :", resultat[1])