#-*- coding: utf_8 -*-
from graphe import *


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

    for i in range(nbExperiences):
        graphe = Graphe(n,p,r) # generation du graphe aléatoire

        if graphe.verifSequenceDestructrice(graphe.trouverSequence()) :
            nbCasPositif += 1

    print("Nombres d'experiences : " +str(nbExperiences))
    print("Nombres de cas positif : "+str(nbCasPositif))
    print("Probabilité d'avoir une séquence 2-destructrice est : %.4f" %(nbCasPositif/nbExperiences))

    return nbCasPositif/nbExperiences

def trouverR(n,p,nbExperiences):

    prob = 0.0 # probabilite qui doit etre le plus proche de 0.5
    varR = 0.0 # valeur particuliere de r à trouver

    while prob < 0.49 or prob > 0.51:
        prob = repeteRandom(n,p,varR,nbExperiences)
        varR += 0.005
        print(" r = %.4f"%varR)

        if varR > 1 :
            varR = 0.0

    print("n = " + str(n) + " p = "+ str(p) + " r = %.4f"%varR)

def main() :

    # graphe = Graphe(10,0.5,0.5)

    # grapheAleatoire(graphe)
    # repeteRandom(10,0.5,0.4236,100)
    trouverR(50,0.7,50)
    


main()

exit()