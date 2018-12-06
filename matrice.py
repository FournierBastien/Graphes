#-*- coding: utf_8 -*-
import random
import numpy as np


class Graphe :

    """
        n : nombre de sommets
        p : probabilité pour les voisins
        r : probabilité pour les couleurs
    """
    def __init__(self, n, p, r):
        # self.graphe = np.random.random_sample((n,n)) # dictionnaire ou liste adjacence
        self.graphe = None
        self.n = n # nombre de sommet -> aléatoire
        self.p = p  # probabilité -> attribution des voisins
        self.r = r # probabilité -> attribution des couleurs
        self.couleurs = []
        self.generer_matrice()
    
    def generer_matrice(self):
        
        self.graphe = np.random.binomial(1, self.p, self.n*self.n).reshape((self.n,self.n))
        self.couleurs = np.random.binomial(1,self.r,self.n)

        for i in range(self.n):
            for j in range(self.n):
                if self.graphe[i][j] == 1 and i != j:
                    self.graphe[j][i] == 1
                if i == j :
                    self.graphe[i][i] = 0
        """
        for i in range(self.n):
            for j in range(self.n):

                if random.random() <= self.p and i != j:
                    self.graphe[j][i] = 1
                    self.graphe[j][i] = 1
                else :
                    self.graphe[i][j] = 0
                    self.graphe[j][i] = 0

        for i in range(self.n):
            if random.random() <= self.r :
                self.couleurs.append(1)
            else :
                self.couleurs.append(0)
        """

        # for i in range(self.n):
        #     for j in range(self.n):
        #         # aretes
        #         if self.graphe[i][j] != 1 and self.graphe[i][j] != 0 and i != j and self.graphe[i][j] <= self.p :
        #             # print("t")
        #             # print(self.graphe[i][j])
        #             # print(i,j)
        #             self.graphe[i][j] = 1
        #             self.graphe[j][i] = 1
        #         elif self.graphe[i][j] != 1 and self.graphe[i][j] != 0 and i != j :
        #             self.graphe[i][j] = 0
        #             self.graphe[j][i] = 0

        #         # couleurs
        #         if i == j and self.graphe[i][j] < self.r :
        #             self.couleurs.append(1) # rouge = 1
        #             self.graphe[i][j] = 0
        #         elif i == j:
        #             self.couleurs.append(0)
        #             self.graphe[i][j] = 0
        
    
    # trouver une sequence 2-destructrice pour le graphe
    def trouverSequence(self) :
        sequence = list()
        listeSommet = list(range(self.n))
        nbVoisins = np.sum(self.graphe,axis=1)
        sommetsRestants = list()
        
        degreInferieur = True
        while degreInferieur :
            degreInferieur = False
            for i in listeSommet :
                if nbVoisins[i] <= 2 :
                    degreInferieur = True
                    sequence.append(i)
                    listeSommet.remove(i)

        # on s'occupe ensuite des sommets qui possède plus de 2 voisins rouge
        # on compte le nombre de voisins rouge qu'ils possèdent et ceux qui en ont le moins
        # sont disposé dans la séquence en premier
        
        for sommet in listeSommet :
            nbVoisinsRougeRestant = 0
            
            for i in listeSommet :
                
                # on regarde si i est voisin de s
                if self.couleurs[i] == 1 and self.graphe[sommet][i] == 1 : 
                    nbVoisinsRougeRestant += 1
            sommetsRestants.append((sommet,nbVoisinsRougeRestant))
        # on trie les valeurs des tuples selon le plus petit nombre de voisins rouge
        sommetsRestants.sort(key=lambda tup: tup[1]) 

        # on ajoute ensuite les sommets restants à la séquence
        for i in sommetsRestants :
            sequence.append(i[0])

        return sequence


    # verifie que la sequence est 2-Destructrice
    def verifSequenceDestructrice(self, sequence):
        
        """
            Pour chaque sommet de la séquence, on regarde si dans la séquence le sommet posssède un voisin de couleur rouge,
            si c'est le cas alors on incrémente le compteur nbVoisinsRougeApres, qui compte le nombre de voisins rouges d'un sommet
            présent après lui dans la séquence
        """
        for i in range(len(sequence)) :
            v = sequence[i]
            nbVoisinsRougeApres = 0 # compteur de voisins rouges après v dans la séquence

            for j in range(i, len(sequence)):
                
                if self.couleurs[sequence[j]] == 1 and self.graphe[v,sequence[j]] == 1 :
                    nbVoisinsRougeApres += 1
                if nbVoisinsRougeApres > 2 :
                    return False
        
        return True

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


"""
TrouverR prend en paramêtre le nombre de sommets n du graphe, p la probabilité pour la création de sommets et arêtes,
et nbExperiences le nombre de d'experiences effectuées dans la fonction repeteRandom pour affiner la variable varR
"""
def trouverR(n,p,nbExperiences):

    prob = 0.0 # probabilite qui doit etre le plus proche de 0.5
    varR = 0.0 # valeur particuliere de r à trouver
    inc = 0.005

    while prob < 0.495 or prob > 0.515:
        prob = repeteRandom(n,p,varR,nbExperiences)
        varR += inc # vitesse d'incrementation
        print(" r = %.4f"%varR)

        # si varR est supérieur à 1 on recommence, idem si la probabilité d'avoir une séquence 2-d est inférieur à 0.45
        # Cela veut dire que l'on a pas trouvé de varR pour lequel prob ~ 0.5 donc on recommence
        if prob < 0.6 and prob > 0.5:
            inc = 0.005
        if prob < 0.495 :
            inc = -0.005

    print("n = " + str(n) + " p = "+ str(p) + " r = %.4f"%varR)

    

def main():
    trouverR(50,0.1,100)
    # graphe = Graphe(10,0.5,0.5)
    # graphe.generer_matrice()

    # print(graphe.graphe)
    # print(graphe.couleurs)

    # a = np.random.binomial(1,0.5,16).reshape((4,4))
    # print(a)

    # c = np.random.binomial(1,0.5,4)
    # print(c)

    # print(np.sum(a,axis=1))

    # t = list([(1,2),(2,3),(1,4),(4,1)])

    # t.sort(key=lambda tup: tup[1])

    # print(t)

    
main()
exit()






# # print(a[:,1])
# d = np.dot(a[:,1],c.reshape(4,))
# print(d)