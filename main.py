#-*- coding: utf_8 -*-
import random
from igraph import *

class Sommet():

    def __init__(self, nom, couleur = None):
        self.nom = nom
        self.couleur = couleur
    
    def setCouleur(self, couleur): # on attribue une couleur au sommet
        self.couleur = couleur

class Graphe():

    def __init__(self, n, p):
        self.graphe = {} # dictionnaire ou liste adjacence
        self.n = n # nombre de sommet -> aléatoire
        self.p = p  # probabilité

        self.intialiserGrapheAleatoire()

    def ajouterSommet(self, sommet):
        
        # on s'assure que sommet n'est pas déjà dans le graphe
        if sommet not in self.graphe.keys() : 
            self.graphe[sommet] = {} # on initialise le sommet dans le graphe sans ces voisins

    def ajouterArrete(self, a, b):
        
        self.graphe[a][b] = b
        self.graphe[b][a] = a

    def intialiserGrapheAleatoire(self):

        for i in range(self.n):
            if random.random() > 0.5 :
                s = Sommet(i,"red")
            else :
                s = Sommet(i,"blue")
            self.ajouterSommet(s)

        # on ajoute les aretes selon la probabilité p
        for i in self.graphe.keys():
            for j in self.graphe.keys() :
                if random.random() > 0.5 and i != j:
                    self.ajouterArrete(i, j)

    def affichageGraphe(self, visualisation):

        # on ajoute les sommets
        visualisation.add_vertices(self.n)

        # on ajoute les aretes
        for i in self.graphe.keys():
            for j in self.graphe[i].keys():
                if random.random() > 0.5 and i != j:  
                    visualisation.add_edges([(i.nom,j.nom)])

    # retourn le degré du sommet
    def degreSommet(self, s):
        return len(self.graphe.keys(s.nom))

    # retourne le nombre de voisins rouge
    def voisinsRouge(self, s):
        iter = 0
        for i in self.graphe.keys(s):
            if i.couleur == "rouge" :
                iter+= 1
        return iter

    # verifie la sequence est 2-Destructrice
    def verifSequenceDestructrice(self, sequence):
        pass
        



graphe = Graphe(10,0.5)

visualisation = Graph()

graphe.affichageGraphe(visualisation)
# visualisation.add_vertices(6)s

# visualisation.add_edges([(2,3),(3,4),(4,5),(5,3)])

# print([ (sommet.nom,sommet.couleur) for sommet in graphe.graphe.keys()])

# sequence aléatoire
sequence = random.sample(range(0,10), 10)

print(sequence)

graphe.verifSequenceDestructrice(sequence)

visual_style = {}

# visualisation.vs['name'] = [ sommet.nom for sommet in graphe.graphe.keys()]
visualisation.vs['label'] = [ sommet.nom for sommet in graphe.graphe.keys()]


visualisation.vs['color'] = [ sommet.couleur for sommet in graphe.graphe.keys()]

print(visualisation)

layout = visualisation.layout("kk")

plot(visualisation, layout = layout, vertex_label_color = "white")