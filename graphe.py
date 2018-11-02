import random

from igraph import *

from sommet import *


class Graphe():

    def __init__(self, n, p, r):
        self.graphe = {} # dictionnaire ou liste adjacence
        self.n = n # nombre de sommet -> aléatoire
        self.p = p  # probabilité
        self.r = r
        self.intialiserGrapheAleatoire()

    def ajouterSommet(self, sommet):
        
        # on s'assure que sommet n'est jpas déjà dans le graphe
        if sommet not in self.graphe.keys() : 
            self.graphe[sommet] = {} # on initialise le sommet dans le graphe sans ces voisins

    def ajouterArrete(self, a, b):
        
        self.graphe[a][b] = b
        self.graphe[b][a] = a

    def intialiserGrapheAleatoire(self):

        # random.random suit une loi binomiale
        for i in range(self.n):
            if random.random() < self.r :
                s = Sommet(i,"red")
            else :
                s = Sommet(i,"blue")
            self.ajouterSommet(s)

        # on ajoute les aretes selon la probabilité p
        for i in self.graphe.keys():
            for j in self.graphe.keys():
                if random.random() < self.p and i != j:
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
    def degreSommet(self, s, list = None):
        return len(self.graphe[s])

    # retourne le nombre de voisins rouge
    def voisinsRouge(self, s, list = None):
        if list :
            nbVoisins = 0
            for i in list:
                if i.couleur == "red" and i in self.graphe[s] :
                    nbVoisins += 1   
            return nbVoisins
        else :
            iter = 0
            for i in self.graphe[s]:
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

    # trouver une sequence 2-destructrice pour le graphe
    def trouverSequence(self) :
        sequence = list()
        listeSommet = list(self.graphe)

        degreInferieur = True
        while degreInferieur :
            degreInferieur = False
            for sommet in listeSommet :
                # on regarde si le sommet a un nb de voisins rouge inferieur ou egale à 2 selon la listeSommet
                # càd les sommets qui n'ont pas encore été disposé dans la séquence
                # si c'est le cas, on met la var booleenne à True car on enleve un sommet de la liste
                # ce qui met à jour les voisins des sommets de cette liste
                if self.voisinsRouge(sommet, listeSommet) <= 2 :
                    degreInferieur = True
                    sequence.append(sommet)
                    listeSommet.remove(sommet)


        # on s'occupe ensuite des sommets qui possède plus de 2 voisins rouge
        # on compte le nombre de voisins rouge qu'ils possèdent et ceux qui en ont le moins
        # sont disposé dans la séquence en premier
        sommetsRestants = list()
        for sommet in listeSommet :
            nbVoisinsRougeRestant = 0
            
            for i in listeSommet :
                # on regarde si i est voisin de s
                if i.couleur == "red" and i in self.graphe[sommet] and i != sommet: 
                    nbVoisinsRougeRestant+= 1
            sommetsRestants.append((sommet,nbVoisinsRougeRestant))
        # on trie les valeurs des tuples selon le plus petit nombre de voisins rouge
        sommetsRestants.sort(key=lambda tup: tup[1]) 

        # on ajoute ensuite les sommets restants à la séquence
        for i in sommetsRestants :
            sequence.append(i[0])

        return sequence