"""
    Algorithms to compare different sort methods (bulle/fusion/rapide)
"""
import random
import time
import sys

sys.setrecursionlimit(1000000)

def make_random_tab(taille_tab):
    """
    Make an array with random number and a size given
    """
    tab_make = []
    for _ in range(taille_tab):
        tab_make.append(random.randint(0, 100))
    return tab_make

def permute(tab_permute, index_a, index_b):
    """
    This function swap two numbers into an array
    """
    temp = tab_permute[index_a]
    tab_permute[index_a] = tab_permute[index_b]
    tab_permute[index_b] = temp
    return tab_permute

def tri_bulle(tab_bulle):
    """
    Sort an array with bubble sort method
    """
    for index_bulle in range(len(tab_bulle)-1, -1, -1):
        for index_bulle_2 in range(index_bulle):
            if tab_bulle[index_bulle] < tab_bulle[index_bulle_2]:
                permute(tab_bulle, index_bulle, index_bulle_2)
    return tab_bulle

def partitionner(tab_part, debut, fin):
    """
    Take a pivot to the begin of the array and swap with the last array's number
    Place lesser number to the begin of the array
    Finaly, swap the first greater number with the pivot
    """
    pivot = tab_part[debut]
    permute(tab_part, debut, fin)
    compteur = debut
    for index_tab in range(debut, fin):
        if tab_part[index_tab] < pivot:
            permute(tab_part, compteur, index_tab)
            compteur += 1
    permute(tab_part, compteur, fin)
    return compteur

def tri_rapide(tab_rapide, debut, fin):
    """
    Sort an array with fast sort method
    """
    if debut < fin:
        pivot = partitionner(tab_rapide, debut, fin)
        tri_rapide(tab_rapide, debut, pivot-1)
        tri_rapide(tab_rapide, pivot+1, fin)
    return tab_rapide

def fusion(tab_a, tab_b):
    """
    Merge two sorted arrays
    """
    if len(tab_b) == 0:
        return tab_a
    if len(tab_a) == 0:
        return tab_b
    if tab_a[0] < tab_b[0]:
        return [tab_a.pop(0)] + fusion(tab_a, tab_b)
    return [tab_b.pop(0)] + fusion(tab_a, tab_b)

def tri_fusion(tab_fusion):
    """
    Sort an array with merge sort methode
    """
    if len(tab_fusion) == 1:
        return tab_fusion
    return fusion(tri_fusion(tab_fusion[:len(tab_fusion)//2]),
                  tri_fusion(tab_fusion[len(tab_fusion)//2:]))

TAILLES_TABLEAU = [10, 100, 1000, 10000, 100000]

for taille in TAILLES_TABLEAU:
    tab_sort = make_random_tab(taille)

    fileWrite = open("benchmark/tri_bulle_"+str(taille)+".txt", "w")
    timeBegin = time.time()
    tri_bulle(tab_sort.copy())
    timeEnd = time.time()
    fileWrite.write(str(timeEnd - timeBegin))
    fileWrite.close()

    fileWrite = open("benchmark/tri_fusion_"+str(taille)+".txt", "w")
    timeBegin = time.time()
    tri_fusion(tab_sort.copy())
    timeEnd = time.time()
    fileWrite.write(str(timeEnd - timeBegin))
    fileWrite.close()

    fileWrite = open("benchmark/tri_rapide_"+str(taille)+".txt", "w")
    timeBegin = time.time()
    tri_rapide(tab_sort.copy(), 0, taille-1)
    timeEnd = time.time()
    fileWrite.write(str(timeEnd - timeBegin))
    fileWrite.close()

    #Average calculation for each sorts with 100 turns

    fileWrite = open("benchmark/average/tri_bulle_"+str(taille)+".txt", "w")
    sommeTimer = 0
    for i in range(100):
        tab_average = make_random_tab(taille)
        timeBegin = time.time()
        tri_bulle(tab_average)
        timeEnd = time.time()
        sommeTimer += (timeEnd - timeBegin)
    fileWrite.write(str(sommeTimer/100))
    fileWrite.close()

    fileWrite = open("benchmark/average/tri_fusion_"+str(taille)+".txt", "w")
    sommeTimer = 0
    for i in range(100):
        tab_average = make_random_tab(taille)
        timeBegin = time.time()
        tri_fusion(tab_average)
        timeEnd = time.time()
        sommeTimer += (timeEnd - timeBegin)
    fileWrite.write(str(sommeTimer/100))
    fileWrite.close()

    fileWrite = open("benchmark/average/tri_rapide_"+str(taille)+".txt", "w")
    sommeTimer = 0
    for i in range(100):
        tab_average = make_random_tab(taille)
        timeBegin = time.time()
        tri_rapide(tab_average, 0, taille-1)
        timeEnd = time.time()
        sommeTimer += (timeEnd - timeBegin)
    fileWrite.write(str(sommeTimer/100))
    fileWrite.close()
