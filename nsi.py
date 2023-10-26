def carre_magique(carre):
    somme_magique = sum(carre[0])
    for i in range(len(carre)):
        if somme_magique != sum(carre[i]) or somme_magique != sum([j[i] for j in carre]):
            return False
    if somme_magique != sum([carre[i][i] for i in range(len(carre))]):
        return False
    if somme_magique != sum([carre[i][len(carre)-i-1] for i in range(len(carre))]):
        return False
    return True
