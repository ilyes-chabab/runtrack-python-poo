import math
class cercle:
    def __init__(self,rayon):
        self.rayon=rayon
    def changerRayon(self,rayon):
        self.rayon=rayon   
    def circonference(self):
        circonf= 2 * math.pi * self.rayon
        print(circonf)
    def aire(self):
        aire = math.pi * self.rayon**2
        print(aire)
    def diametre(self):
        diametre= 2*self.rayon
        print(diametre)
    def afficherInfos(self):
        print(f"diametre : {2*self.rayon} , rayon : {self.rayon} ,circonférence :{ 2 * math.pi * self.rayon} , aire : {math.pi * self.rayon**2} , ")
cercle1=cercle(4)
print("Cercle 1 :")
cercle1.afficherInfos()
cercle1.diametre()
cercle1.circonference()
cercle1.aire()
cercle2=cercle(7)
print("Cercle 2 :")
cercle2.afficherInfos()
cercle2.diametre()
cercle2.circonference()
cercle2.aire()




        