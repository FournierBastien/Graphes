#-*- coding: utf_8 -*-
from graphe import *

# Optionnel, graphe aleatoire où chaque arete a une probabilité p d'appartenir au graphe
# Attention utilise la librairie igraph
def visualisationGrapheAleatoire(n,p,r) :

    graphe = Graphe()
    graphe.intialiserGrapheAleatoire(n,p,r)
    # graphe.affichageGrapheAleatoire()


# calcul de la probabilite d'avoir une séquence 2-destructrice
def repeteRandom(n,p,r,nbExperiences):

    nbCasPositif = 0

    for _ in range(nbExperiences):
        graphe = Graphe() # generation du graphe aléatoire
        graphe.intialiserGrapheAleatoire(n,p,r)
        sequence = graphe.trouverSequence()
        # print(resultat)
        if graphe.verifSequenceDestructrice(sequence) :
            nbCasPositif += 1

    # print("Nombres d'experiences : " +str(nbExperiences))
    # print("Nombres de cas positif : "+str(nbCasPositif))
    # print("Probabilité d'avoir une séquence 2-destructrice est : %.4f" %(nbCasPositif/nbExperiences))

    return nbCasPositif/nbExperiences

"""
TrouverR prend en paramêtre le nombre de sommets n du graphe, p la probabilité pour la création de sommets et arêtes,
et nbExperiences le nombre de d'experiences effectuées dans la fonction repeteRandom pour affiner la variable varR

version dichotomique
    # Ici, on fait varier la variable sur deux intervalles
    # la variable r qui obtient une probabilité plus proche de 0.5 est sélectionner
    # puis on recrée un nouvel intervalle à partir de cette variable r
"""
def trouverRDichotomie(n,p,nbExperiences):

    varR = 0.0 # valeur particuliere de r à trouver

    interval_r = 1
    interval_sup_r = interval_r
    interval_inf_r = interval_r/2
    
    prob_inf = 0
    prob_sup = 0

    while (prob_sup < 0.4951 or prob_sup > 0.5051) and (prob_inf < 0.4951 or prob_inf > 0.5051)  : 

        prob_sup = repeteRandom(n,p,interval_sup_r,nbExperiences)
        prob_inf = repeteRandom(n,p,interval_inf_r,nbExperiences)

        # print(interval_sup_r, prob_sup)
        # print(interval_inf_r, prob_inf)

        interval_r = interval_r/2
        if abs(0.5 - prob_sup) < abs(0.5 - prob_inf) :          
            interval_sup_r = abs(interval_sup_r + interval_r/2)
            interval_inf_r = abs(interval_sup_r - interval_r)
        else :
            interval_sup_r = abs(interval_inf_r + interval_r/2)
            interval_inf_r = abs(interval_inf_r - interval_r/2)

    if prob_sup > 0.4951 and prob_sup < 0.5051 :
        # print("n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(interval_sup_r*100))
        return interval_sup_r
    if prob_inf > 0.4951 and prob_inf < 0.5051 :
        # print("n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(interval_inf_r*100))
        return interval_inf_r
    
    
"""
version itérative
    # Ici, on fait varier la valeur varR pour trouver une valeur de la variable prob proche de 0.5
    # Si prob est supérieur à 0.6, l'incrémentation se fait plus rapidement
    # Si prob est inférieur à 0.6, on diminue le rithme d'incrémentation pour être plus précis
    # Si prob est inférieur à 0.4, on incrémente à l'envers pour revenir vers des valeur de prob proche de 0.5
"""
def trouverRIteratif(n,p,nbExperiences) :
    varR = 0.0 # valeur particuliere de r à trouver   
    interval_r = 1

    prob = 0.0 # probabilite qui doit etre le plus proche de 0.5
    inc = 0.01
    while prob < 0.495 or prob > 0.505:
        prob = repeteRandom(n,p,varR,nbExperiences)
        
        varR += inc # vitesse d'incrementation
        # print(" r = %.4f"%varR)

        # si varR est supérieur à 1 on recommence, idem si la probabilité d'avoir une séquence 2-d est inférieur à 0.45
        # Cela veut dire que l'on a pas trouvé de varR pour lequel prob ~ 0.5 donc on recommence
        
        if prob < 0.6 and prob > 0.5:
            inc = 0.0001
        if prob < 0.495 :
            inc = -0.0001

    print("n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(varR*100))

def algoTrouverLesRD() :
    trouverRDichotomie(50,0.1,800)
    trouverRDichotomie(100,0.1,800)
    trouverRDichotomie(50,0.3,800)
    trouverRDichotomie(100,0.3,800)
    trouverRDichotomie(50,0.5,800)
    trouverRDichotomie(100,0.5,800)
    trouverRDichotomie(50,0.7,800)
    trouverRDichotomie(100,0.7,800)

def algoTrouverLesRI() :
    trouverRIteratif(50,0.1,800)
    trouverRIteratif(100,0.1,800)
    trouverRIteratif(50,0.3,800)
    trouverRIteratif(100,0.3,800)
    trouverRIteratif(50,0.5,800)
    trouverRIteratif(100,0.5,800)
    trouverRIteratif(50,0.7,800)
    trouverRIteratif(100,0.7,800)

"""
Qui étant donné n,p,r en paramètre, retourne la probabilité qu'un graphe, où chaque sommet a une probabilité r d'être rouge, 
admette une séquence 2-destructrice.
"""
def testA(n,p,r) :

    moyenne = repeteRandom(n,p,r,800)      
    print("TestA : probabilité d'avoir une séquence 2-destructrice = %.2f" %(moyenne*100))

"""
Qui étant donné n,p,r en paramètre, retourne la valeur de r pour laquelle si la proportion de sommets rouges est r, alors le graphe a une probabilité proche de 1/2
d'avoir une séquence 2-destructrice
"""
def testB(n,p) :
    r = trouverRDichotomie(n,p,800)
    print("TestB : n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(r*100))


def main() :

    testA(50,0.5,0.2)
    # testB(50,0.5)
    

main()

exit()
