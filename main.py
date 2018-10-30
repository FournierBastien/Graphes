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
        
        # on s'assure que sommet n'est jpas déjà dans le graphe
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
            for j in self.graphe.keys():
                if random.random() > 0.5 and i != j:
                    self.ajouterArrete(i, j)

    def affichageGraphe(self, visualisation):

        # on ajoute les sommets
        visualisation.add_vertices(self.n)

        # on ajoute les aretes
        for i in self.graphe.keys():
            for j in self.graphe[i].keys():
                # permet de ne pas avoir de doublons
                # si l'arete existe déjà on ne l'a crée pas 
                if visualisation.get_eid(j.nom, i.nom, directed=False, error=False) == -1 :
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
    
    # verifie si s2 est voisin de s1
    def estVoisin(self, s1, s2):
        if s2 in self.graphe[s1] : 
            return True
        else : 
            return False

    def getSommet(self, nom) :
        for i in self.graphe :
            if i.nom == nom :
                return i
        return None

    # verifie que la sequence est 2-Destructrice
    def verifSequenceDestructrice(self, sequence):
        
        for i in range(len(sequence)) :
            v = sequence[i]
            nbVoisinsRougeApres = 0 # compteur de voisins rouges après v dans la séquence
        
            for j in range(i, len(sequence)):
                if sequence[j].couleur == "red" and self.estVoisin(v,sequence[j]) :
                    nbVoisinsRougeApres += 1
                if nbVoisinsRougeApres > 2 :
                    return False
        
        return True

    def generationSequence(self) :
        randomList = random.sample(range(0,self.n), self.n)
        sequence = {}

        for i in range(self.n):
            sequence[i] = self.getSommet(randomList[i]) 

        return sequence

graphe = Graphe(10,0.5)

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

# visualisation.vs['name'] = [ sommet.nom for sommet in graphe.graphe.keys()]
visualisation.vs['label'] = [ sommet.nom for sommet in graphe.graphe.keys()]


visualisation.vs['color'] = [ sommet.couleur for sommet in graphe.graphe.keys()]

print(visualisation)

layout = visualisation.layout("kk")

# plot(visualisation, layout = layout, vertex_label_color = "white")

visualisation.write_dot("todo.dot")