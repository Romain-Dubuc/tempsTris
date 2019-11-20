"""
    Graph et temps de calcul moyenne
    Mettre des commentaires
    Faire le pdf
"""
import random
import time
import sys

sys.setrecursionlimit(10000)

"""
    Make an array with random number and a size given
"""
def makeRandomTab(taille):
    tab = []
    for i in range(taille):
        tab.append(random.randint(0, 100))
    return tab

"""
    This function swap two numbers into an array
"""
def permute(tab, indexA, indexB):
    temp = tab[indexA]
    tab[indexA] = tab[indexB]
    tab[indexB] = temp
    return tab

"""
    Sort an array with bubble sort method
"""
def triBulle(tab):
    for i in range(len(tab)-1, -1, -1):
        for j in range(i):
            if (tab[i] < tab[j]):
                permute(tab, i, j)
    return tab

"""

"""
def partitionner(tab, debut, fin):
    pivot = tab[debut]
    permute(tab, debut, fin)
    compteur = debut
    for i in range(debut, fin):
        if (tab[i] < pivot):
            permute(tab, compteur, i)
            compteur += 1
    permute(tab, compteur, fin)
    return compteur

"""
    Sort an array with fast sort method
"""
def triRapide(tab, debut, fin):
    if (debut < fin):
        pivot = partitionner(tab, debut, fin)
        triRapide(tab, debut, pivot-1)
        triRapide(tab, pivot+1, fin)
    return tab

def insertValue(tab, value, cpt = 0):
    if (len(tab) == cpt or tab[cpt] > value):
        tab.insert(cpt, value)
        return tab
    insertValue(tab, value, cpt+1)

def fusion(tabA, tabB):
    if (len(tabB) == 0):
        return tabA
    insertValue(tabA, tabB.pop())
    return fusion(tabA, tabB)

"""
    Sort an array with fusion sort methode
"""
def triFusion(tab):
    if (len(tab) == 1):
        return tab
    return fusion(triFusion(tab[:len(tab)//2]), triFusion(tab[len(tab)//2:]))

taillesTableau = [10, 100, 1000, 10000, 100000]

for taille in taillesTableau:
    tab = makeRandomTab(taille)
    
    fileWrite = open("benchmark/triBulle_"+str(taille)+".txt", "w")
    timeBegin = time.time()
    triBulle(tab.copy())
    timeEnd = time.time()
    fileWrite.write(str(timeEnd - timeBegin))
    fileWrite.close()

    fileWrite = open("benchmark/triFusion_"+str(taille)+".txt", "w")
    timeBegin = time.time()
    triFusion(tab.copy())
    timeEnd = time.time()
    fileWrite.write(str(timeEnd - timeBegin))
    fileWrite.close()

    fileWrite = open("benchmark/triRapide_"+str(taille)+".txt", "w")
    timeBegin = time.time()
    triRapide(tab.copy(), 0, taille-1)
    timeEnd = time.time()
    fileWrite.write(str(timeEnd - timeBegin))
    fileWrite.close()

    #Calcul average for each sorts with 100 turns
    fileWrite = open("benchmark/average/triBulle_"+str(taille)+".txt", "w")
    sommeTimer = 0
    for i in range(100):
        tab2 = makeRandomTab(taille)
        timeBegin = time.time()
        triBulle(tab2)
        timeEnd = time.time()
        sommeTimer += (timeEnd - timeBegin)
    fileWrite.write(str(sommeTimer/100))
    fileWrite.close()

    fileWrite = open("benchmark/average/triFusion_"+str(taille)+".txt", "w")
    sommeTimer = 0
    for i in range(100):
        tab2 = makeRandomTab(taille)
        timeBegin = time.time()
        triFusion(tab2)
        timeEnd = time.time()
        sommeTimer += (timeEnd - timeBegin)
    fileWrite.write(str(sommeTimer/100))
    fileWrite.close()

    fileWrite = open("benchmark/average/triRapide_"+str(taille)+".txt", "w")
    sommeTimer = 0
    for i in range(100):
        tab2 = makeRandomTab(taille)
        timeBegin = time.time()
        triRapide(tab2, 0, taille-1)
        timeEnd = time.time()
        sommeTimer += (timeEnd - timeBegin)
    fileWrite.write(str(sommeTimer/100))
    fileWrite.close()
