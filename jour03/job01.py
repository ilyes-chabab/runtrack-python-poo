class Ville:
    def __init__(self,nomVille,nombreHabitant):
        self.__nomVille=nomVille
        self.__nombreHabitant=nombreHabitant
    def afficherVille(self):
        print(f"ville : {self.__nomVille} ,{self.__nombreHabitant} habitants")
    def getHabitant(self):
        return self.__nombreHabitant
    def getVille(self):
        return self.__nomVille
    def setHabitant(self,nombreHabitant):
        self.__nombreHabitant=nombreHabitant

    
class personne:
    def __init__(self,nom,age,ville):
        self.__nom=nom
        self.__age=age
        self.__ville= ville
    def ajouterPopulation(self, ville):
        ajout = ville.getHabitant() + 1
        ville.setHabitant(ajout)
        print(f"modification pour la ville de {ville.getVille()} , {ville.getHabitant()} habitants")

paris=Ville("paris",1000000)
paris.afficherVille()
marseille=Ville("Marseille",861635)
marseille.afficherVille()
John=personne("John" ,45,paris)
John.ajouterPopulation(paris)
myrtille=personne("myrtille", 4 , paris)
myrtille.ajouterPopulation(paris)
chloe=personne("chloé",18 ,marseille)
chloe.ajouterPopulation(marseille)



        
