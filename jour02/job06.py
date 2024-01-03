class animal:
    def __init__(self,age,prenon):
        self.age=0
        self.prenom=""
    def vieillir(self):
        self.age +=1
    def nommer(self,prenom):
        self.prenom=prenom      
bestial=animal(0,"animal")
print(f"l'age de l'animal avant vieillissement : {bestial.age}")
bestial.vieillir()
print(f"l'age de l'animal apres vieillissement : {bestial.age}")
bestial.nommer("spiderman")
print(f"l'animal se nomme {bestial.prenom}")

