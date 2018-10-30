class Sommet():

    def __init__(self, nom, couleur = None):
        self.nom = nom
        self.couleur = couleur
    
    def setCouleur(self, couleur): # on attribue une couleur au sommet
        self.couleur = couleur