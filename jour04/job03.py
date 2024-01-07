class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    def perimètre(self):
        print("périmetre :", 2*(self.__longueur+self.__largeur))
    def surface(self):
        print("surface :", self.__longueur * self.__largeur)
    def getLongueur(self):
        return self.__longueur
    def getLargeur(self):
        return self.__largeur
    def setLongueur(self,longueur):
        self.__longueur=longueur
    def setLargeur(self,largeur):
        self.__largeur=largeur
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        Rectangle.__init__(longueur, largeur)
        self.hauteur=hauteur
    def volume(self):
        print("volume :",self.__longueur*self.__largeur*self.hauteur)
rect=Rectangle(100,50)
rect.perimètre()
rect.surface()
    