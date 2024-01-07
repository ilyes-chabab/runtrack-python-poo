class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque=marque
        self.modele=modele
        self.annee = annee
        self.prix=prix
    def informationsVehicule(self):
        print(self.marque,self.modele,self.annee,self.prix)
    def demarrer(self):
        print("Attention, je roule")
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self,marque, modele, annee, prix)
        self.porte=4
    def informationsVehicule(self):
        print(self.marque,self.modele,self.annee,self.prix,self.porte)
    def demarrer(self):
        print("Attention je vroum vroum")
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self,marque, modele, annee, prix)
        self.roue=2
    def informationsVehicule(self):
        print(self.marque,self.modele,self.annee,self.prix,self.roue)
    def demarrer(self):
        print("Attention je brrrrrrrrrr")
merco=Voiture("mercedes","classe A", 2020 , 18500)
merco.informationsVehicule()
merco.demarrer()
yamaha=Moto("yamaha","1200 vmx" , 1987, 4500)
yamaha.informationsVehicule()
yamaha.demarrer()

    

