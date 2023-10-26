def carre_magique(carre):
    for i in carre[1:]:
        if sum(carre[0]) != sum(i):
            return False
    for i in range(len(carre)):
        if sum(carre[0]) != sum([j[i] for j in carre]):
            return False
    if sum(carre[0]) != sum([carre[i][i] for i in range(len(carre))]):
        return False
    if sum(carre[0]) != sum([carre[i][len(carre)-i-1] for i in range(len(carre))]):
        return False
    return True
