class personne:
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
    def sepresenter(self):
        return self.nom + self.prenom
ilyes=personne("Chabab"," Ilyes")
print(f"je suis {ilyes.sepresenter()}")
john=personne("Cena"," John")
print(f"je suis {john.sepresenter()}")