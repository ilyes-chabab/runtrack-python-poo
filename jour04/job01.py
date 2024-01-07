class Personne:
    def __init__(self):
        self.age=14
    def afficherAge(self):
        print(f"{self.age} ans")
    def bonjour(self):
        print("Hello")
    def modifierAge(self,nombre):
        self.age = nombre
class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
    def allerEnCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print(f"j'ai {self.age} ans")
class Professeur:
    def __init__(self,matiereEnseignee,):
        self.matiereEnseignee:matiereEnseignee
    def enseigner(self):
        print("Le cours va commencer")
eleve1=Personne()
eleve1.modifierAge(30)
eleve1.afficherAge()
eleve2=Eleve()
eleve2.afficherAge()
        
