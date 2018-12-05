#-*- coding: utf_8 -*-
from graphe import *
import numpy as np


# graphe aleatoire où chaque arete a une probabilité p d'appartenir au graphe
#
def grapheAleatoire(graphe) :
    
    visualisation = Graph()

    graphe.affichageGraphe(visualisation)

    # sequence aléatoire
    sequence = graphe.generationSequence()

    sequenceTrouver = graphe.trouverSequence()
    VerfiSequenceTrouver = graphe.verifSequenceDestructrice(sequenceTrouver)

    print("Sequence trouver : " + ' '.join(str(i.nom) for i in sequenceTrouver))
    if VerfiSequenceTrouver :
        print("Le graphe possède une séquence 2-destructrice !")
    else :
        print("Le graphe ne possède pas de séquence 2-destructrice !")
    # verfication sequence destructrice
    result = graphe.verifSequenceDestructrice(sequence)

    print('sequence : ' +  ' ' .join(str(sequence[i].nom)+'('+sequence[i].couleur+')' for i in sequence))
    print('La séquence est 2-Destructrice : ' + str(result))
    # print(' ' .join(str(i.nom) for i in graphe.graphe[graphe.getSommet(1)]))

    visual_style = {}
    visualisation.vs['label'] = [ sommet.nom for sommet in graphe.graphe.keys()]
    visualisation.vs['color'] = [ sommet.couleur for sommet in graphe.graphe.keys()]
    layout = visualisation.layout("kk")
    # print(visualisation)
    plot(visualisation, layout = layout, vertex_label_color = "white")
    # visualisation.write_dot("todo.dot")


# calcul de la probabilite d'avoir une séquence 2-destructrice
def repeteRandom(n,p,r,nbExperiences):

    nbCasPositif = 0

    for _ in range(nbExperiences):
        graphe = Graphe(n,p,r) # generation du graphe aléatoire
        sequence = graphe.trouverSequence()
        # print(resultat)
        if graphe.verifSequenceDestructrice(sequence) :
            nbCasPositif += 1

    print("Nombres d'experiences : " +str(nbExperiences))
    print("Nombres de cas positif : "+str(nbCasPositif))
    print("Probabilité d'avoir une séquence 2-destructrice est : %.4f" %(nbCasPositif/nbExperiences))

    return nbCasPositif/nbExperiences

"""
TrouverR prend en paramêtre le nombre de sommets n du graphe, p la probabilité pour la création de sommets et arêtes,
et nbExperiences le nombre de d'experiences effectuées dans la fonction repeteRandom pour affiner la variable varR
"""
def trouverR(n,p,nbExperiences):

    prob = 0.0 # probabilite qui doit etre le plus proche de 0.5
    varR = 0.0 # valeur particuliere de r à trouver
    inc = 0.01

    interval_r = 1
    interval_sup_r = interval_r
    interval_inf_r = interval_r/2
    
    prob_inf = 0
    prob_sup = 0

    while True:

        prob_sup = repeteRandom(n,p,interval_sup_r,nbExperiences)
        prob_inf = repeteRandom(n,p,interval_inf_r,nbExperiences)

        print(interval_sup_r, prob_sup)
        print(interval_inf_r, prob_inf)

        interval_r = interval_r/2
        if abs(0.5 - prob_sup) < abs(0.5 - prob_inf) :          
            interval_sup_r = abs(interval_sup_r + interval_r/2)
            interval_inf_r = abs(interval_sup_r - interval_r/2)
        else :
            print("inf")
            interval_sup_r = abs(interval_inf_r + interval_r/2)
            interval_inf_r = abs(interval_inf_r - interval_r/2)

        if prob_sup < 0.4999 and prob_sup > 0.5001 :
            print("n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(interval_sup_r*100))
            return
        if prob_inf < 0.4999 and prob_inf > 0.5001 :
            print("n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(interval_inf_r*100))
            return
    # while prob < 0.4999 or prob > 0.5001:
    #     prob = repeteRandom(n,p,varR,nbExperiences)
        
    #     varR += inc # vitesse d'incrementation
    #     print(" r = %.4f"%varR)

    #     # si varR est supérieur à 1 on recommence, idem si la probabilité d'avoir une séquence 2-d est inférieur à 0.45
    #     # Cela veut dire que l'on a pas trouvé de varR pour lequel prob ~ 0.5 donc on recommence
        

    #     if prob < 0.6 and prob > 0.5:
    #         inc = 0.0005
    #     if prob < 0.495 :
    #         inc = -0.0001

    # print("n = " + str(n) + " p = "+ str(p) + " r = %.2f"%(varR*100))

def main() :

    # graphe = Graphe(10,0.5,0.5)

    # t = [(2,1),(3,list())]
    # l = list([(2,1),(3,2)])

    # t.append((2,1))
    # print(type(t),type(l))

    # t[1][1].append(1)
    # print(t)
    # print(t[1][1][0])
    # print(l[1][1])

    # grapheAleatoire(graphe)
    # repeteRandom(10,0.5,0.4236,100)
    trouverR(50,0.1,800)
    # s = np.random.binomial(1, 0.5, 100)
    # graphe.afficher()
    # print(s)

    # print(sum(np.random.binomial(1, 0.1, 200) == 0)/200)
    # t = np.random.binomial(1, 0.1, 100).reshape((10,10))

    # print(t)


main()

exit()
