class rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def mutateur(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def afficher(self):
        print(f"longueur : {self.__longueur} , largeur: {self.__largeur}")
rect=rectangle(10,5)
rect.afficher()
rect.mutateur(15,10)
rect.afficher()