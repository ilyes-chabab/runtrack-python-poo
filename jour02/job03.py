class livre:
    def __init__(self,titre,auteur,NombreDePage):
        self.__titre=titre
        self.__auteur=auteur
        self.__NombreDePage=NombreDePage
        self.__disponible=True
    def ChangerTitre(self,titre):
        self.__titre=titre
    def ChangerAuteur(self,auteur):
        self.__auteur=auteur
    def ChangerNombreDePage(self,NombreDePage):
        if NombreDePage >0 :
            self.__NombreDePage=NombreDePage
        else:
            print("Erreur : La page doit etre un entier positif.")   
    def afficher(self):
        print(f"Titre : {self.__titre} , Auteur: {self.__auteur} , Nombre de page : {self.__NombreDePage}  ")
    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.verification():         
            print("Livre emprunté !") 
            self.__disponible == False
        else:
            print("Ce livre n'est pas disponible")
    def rendre(self):
        if not self.verification():
            print("Livre rendu !")
            self.__disponible = True       
        else:
            print("Ce livre n'a pas été emprunté")
FleurDuMal=livre("Les fleur du mal","Charles Baudelaire",214)
FleurDuMal.afficher()
FleurDuMal.ChangerNombreDePage(-12)
FleurDuMal.afficher()
FleurDuMal.rendre()
FleurDuMal.emprunter()

