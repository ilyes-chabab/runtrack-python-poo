class produit:
    def __init__(self,nom, prixHT,TVA):
        self.nom=nom
        self.prixHT=prixHT
        self.TVA= TVA
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.prixHT * (self.TVA / 100))
        return prixTTC
    def afficher(self):
        infos= f"nom : {self.nom} , prix TTC : {self.CalculerPrixTTC()}"
        return infos
    def ChangerNom(self,nom):
        self.nom = nom
    def ChangerPrixHT(self,prixHT):
        self.prixHT=prixHT
    
chips=produit("chips",100,50)
chips.ChangerPrixHT(50)
print(chips.afficher())

sandwich=produit("sandwich",200,20)
sandwich.ChangerNom("hamburger")
print(sandwich.afficher())

dessert=produit("dessert",150,30)
print(dessert.afficher())

        