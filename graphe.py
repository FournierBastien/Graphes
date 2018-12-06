import random
import numpy as np

from igraph import *

# from sommet import *


class Graphe():

    def __init__(self, n, p, r):
        self.graphe = [] # dictionnaire ou liste adjacence
        self.n = n # nombre de sommet -> aléatoire
        self.p = p  # probabilité -> attribution des voisins
        self.r = r # probabilité -> attribution des couleurs
        self.couleurs = []
        self.intialiserGrapheAleatoire()

    def ajouterSommet(self, sommet):
        
        # on s'assure que sommet n'est jpas déjà dans le graphe
        if sommet not in self.graphe.keys() : 
            self.graphe = {} # on initialise le sommet dans le graphe sans ces voisins

    def afficher(self):

        for i in self.graphe.keys():
            print("Sommets :" + str(i.nom) + " Voisins :")
            
            for j in self.graphe[i].keys():
                print(" " + str(j.nom))
                
            print("\n")

    def ajouterArrete(self, a, b):
              
        self.graphe[a][1].append(b)
        self.graphe[b][1].append(a)
        

    def intialiserGrapheAleatoire(self):

        self.couleurs = np.random.binomial(1,self.r,self.n)    
        
        # random.random suit une loi binomiale
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

        # on ajoute les sommets
        visualisation.add_vertices(self.n)

        # on ajoute les aretes
        for i in self.graphe.keys():
            for j in self.graphe[i].keys():
                # permet de ne pas avoir de doublons
                # si l'arete existe déjà on ne l'a crée pas 
                if visualisation.get_eid(j.nom, i.nom, directed=False, error=False) == -1 :
                    visualisation.add_edges([(i.nom,j.nom)])

    # retourne le nombre de voisins rouge
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
    
    # verifie si s2 est voisin de s1
    def estVoisin(self, s1, s2):
        if s2 in self.graphe[s1][1] : 
            return True
        else : 
            return False

    # verifie que la sequence est 2-Destructrice
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

    def generationSequence(self) :
        randomList = random.sample(range(0,self.n), self.n)
        sequence = {}

        for i in range(self.n):
            pass
            # sequence[i] = self.getSommet(randomList[i]) 

        return sequence

    # trouver une sequence 2-destructrice pour le graphe
    def trouverSequence(self) :
        sequence = list()
        listeSommet = [i for i in range(self.n)]

        degreInferieur = True
        while degreInferieur :
            degreInferieur = False
            for i in listeSommet :
                # on regarde si le sommet a un nb de voisins rouge inferieur ou egale à 2 selon la listeSommet
                # càd les sommets qui n'ont pas encore été disposé dans la séquence
                # si c'est le cas, on met la var booleenne à True car on enleve un sommet de la liste
                # ce qui met à jour les voisins des sommets de cette liste
                if self.voisinsRouge(i, listeSommet) <= 2 :
                    degreInferieur = True
                    sequence.append(i)
                    listeSommet.remove(i)

        # on s'occupe ensuite des sommets qui possède plus de 2 voisins rouge
        # on compte le nombre de voisins rouge qu'ils possèdent et ceux qui en ont le moins
        # sont disposé dans la séquence en premier
        # sommetsRestants = list()
        fin = False
        it = 0
        
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
        
        # on trie les valeurs des tuples selon le plus petit nombre de voisins rouge

        # on ajoute ensuite les sommets restants à la séquence
    
        # on teste ensuite la validité de cette séquence 
        # si elle n'est pas 2-destructrice, on teste toutes les combinaisons


        