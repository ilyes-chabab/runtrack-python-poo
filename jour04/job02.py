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
class Professeur(Personne):
    def __init__(self):
        self.__matiereEnseignee="mathématique"
    def enseigner(self):
        print("Le cours va commencer")
eleve1=Eleve()
eleve1.modifierAge(30)
eleve1.afficherAge()
eleve1.bonjour()
eleve1.allerEnCours()
prof1=Professeur()
prof1.modifierAge(40)
prof1.bonjour()
prof1.enseigner()