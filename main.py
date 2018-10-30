#-*- coding: utf_8 -*-
from graphe import *

def grapheAleatoire(graphe) :
    
    visualisation = Graph()

    graphe.affichageGraphe(visualisation)

    # sequence aléatoire
    sequence = graphe.generationSequence()

    # verfication sequence destructrice
    result = graphe.verifSequenceDestructrice(sequence)

    print('sequence : ' +  ' ' .join(str(sequence[i].nom)+'('+sequence[i].couleur+')' for i in sequence))
    print('La séquence est 2-Destructrice : ' + str(result))
    print(' ' .join(str(i.nom) for i in graphe.graphe[graphe.getSommet(1)]))

    if graphe.getSommet(3) in graphe.graphe[graphe.getSommet(1)] :
        print('lol')

    visual_style = {}
    visualisation.vs['label'] = [ sommet.nom for sommet in graphe.graphe.keys()]
    visualisation.vs['color'] = [ sommet.couleur for sommet in graphe.graphe.keys()]
    layout = visualisation.layout("kk")
    # print(visualisation)
    plot(visualisation, layout = layout, vertex_label_color = "white")
    # visualisation.write_dot("todo.dot")


def main() :

    graphe = Graphe(10,0.5)

    algo1(graphe)

    


main()

exit()