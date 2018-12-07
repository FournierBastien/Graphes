import random
import numpy as np

from igraph import *

# from sommet import *


class Graphe():

    def __init__(self, n, p, r):
        self.graphe = [] # liste adjacence
        self.n = n # nombre de sommet 
        self.p = p  # probabilité pour l'attribution des voisins
        self.r = r # probabilité pour l'attribution des couleurs
        self.couleurs = []
        self.intialiserGrapheAleatoire()

    def ajouterArrete(self, a, b):
              
        self.graphe[a][1].append(b)
        self.graphe[b][1].append(a)
        
    """
    Initialisation du graphe selon une loi binomiale pour les couleurs de chaque sommet
    et une loi binomiale pour les arêtes
    La fonction np.random.binomiale nous renvoie un tableau comprenant le resultat d'experience d'une loi binomiale selon
    l'interval des valeurs, ici 0 ou 1, la probabilité d'avoir 1 dans le tableau (self.r ou self.p) et le nombre d'experience
    à effectuer, c'est à dire la taille du tableau de sortie
    """
    def intialiserGrapheAleatoire(self):

        self.couleurs = np.random.binomial(1,self.r,self.n)    
        
        for i in range(self.n):
            self.graphe.append((i,list()))  
        
        voisins_aleatoire = np.random.binomial(1, self.p, int(self.n*(self.n-1)/2))
        iter = 0
        for i in range(self.n) :
            for j in range(i+1,self.n):
                if voisins_aleatoire[iter] == 1 :
                    self.graphe[i][1].append(j)
                    self.graphe[j][1].append(i)
                iter += 1


    def affichageGraphe(self, visualisation):
        pass
        # # on ajoute les sommets
        # visualisation.add_vertices(self.n)

        # # on ajoute les aretes
        # for i in self.graphe.keys():
        #     for j in self.graphe[i].keys():
        #         # permet de ne pas avoir de doublons
        #         # si l'arete existe déjà on ne l'a crée pas 
        #         if visualisation.get_eid(j.nom, i.nom, directed=False, error=False) == -1 :
        #             visualisation.add_edges([(i.nom,j.nom)])

    """
    retourne le nombre de voisins rouge de s au total ou dans la liste donnée en paramètre
    """
    def voisinsRouge(self, s, list = None):
        if list :
            nbVoisins = 0
            for i in list:
                if self.couleurs[i] == 1 and i in self.graphe[s][1]:
                    nbVoisins += 1   
            return nbVoisins
        else :
            iter = 0
            for i in self.graphe[s][1]:
                if self.couleurs[i] == 1 :
                    iter+= 1
            return iter
    
    """
    verifie si s2 est voisin de s1
    """
    def estVoisin(self, s1, s2):
        if s2 in self.graphe[s1][1] : return True
        else : return False

    """
    verifie que la sequence est 2-Destructrice
    """
    def verifSequenceDestructrice(self, sequence):
        
        """
            Pour chaque sommet de la séquence, on regarde si dans la séquence le sommet posssède un voisin de couleur rouge,
            si c'est le cas alors on incrémente le compteur nbVoisinsRougeApres, qui compte le nombre de voisins rouges d'un sommet
            présent après lui dans la séquence
        """
        if len(sequence) < self.n or len(sequence) > self.n:
            return False

        for i in range(len(sequence)) :
            v = sequence[i]
            nbVoisinsRougeApres = 0 # compteur de voisins rouges après v dans la séquence
        
            for j in range(i, len(sequence)):
                if self.couleurs[sequence[j]] == 1 and self.estVoisin(v,sequence[j]) :
                    nbVoisinsRougeApres += 1
            if nbVoisinsRougeApres > 2 :
                return False
        
        return True

    """
    Génération aléatoire d'une séquence
    """
    def generationSequence(self) :
        randomList = random.sample(range(0,self.n), self.n)
        sequence = {}

        for i in range(self.n):
            sequence[i] = randomList[i] 

        return sequence

    """
    trouver une sequence 2-destructrice dans le graphe
    """
    def trouverSequence(self) :
        sequence = list()
        listeSommet = [i for i in range(self.n)]

        degreInferieur = True

        """
        on regarde si le sommet a un nb de voisins rouge inferieur ou egale à 2 selon la listeSommet
        c'est à dire les sommets qui n'ont pas encore été disposé dans la séquence
        si c'est le cas, on met la var booleenne à True car on enleve un sommet de la liste
        et on réitère la boucle jusqu'à ce qu'on n'ajoute plus de sommet à la séquence
        """
        while degreInferieur :
            degreInferieur = False
            for i in listeSommet :
                if self.voisinsRouge(i, listeSommet) <= 2 :
                    degreInferieur = True
                    sequence.append(i)
                    listeSommet.remove(i)


        """
        On s'occupe ensuite des sommets qui possèdent plus de 2 voisins rouge.
        On va compter le nombre de voisins rouge que possède un sommet dans la liste des sommets n'ayant pas
        été ajouté à la séquence. Si un sommet possède au plus de 2 voisins rouge restant alors on l'ajoute à la séquence et on réitère la boucle
        sinon on termine la boucle
        """

        fin = False
        while fin == False :
            fin = True
            for sommet in listeSommet :
                nbVoisinsRougeRestant = 0
                
                for i in listeSommet :
                    # on regarde si i est voisin de s
                    
                    if i != sommet and self.couleurs[i] == 1 and self.estVoisin(sommet,i) : 
                        nbVoisinsRougeRestant += 1
                if nbVoisinsRougeRestant <= 2 :
                    fin = False
                    sequence.append(sommet)
                    listeSommet.remove(sommet)
        return sequence
        