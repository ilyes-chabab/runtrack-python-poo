class Personnage:
    def __init__(self,nom,vie):
        self.nom=nom
        self.vie=vie
    def attaquer(self,ennemi):
        ennemi.vie -= 10
        print(f"vie de {ennemi} : {ennemi.vie}")
    def __str__(self):
        return self.nom


class Jeu:
    def __init__(self):
        self.niveau = 1
        self.joueurs=[]
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))
    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == 1:
            joueur=Personnage("joueur",30)
            ennemi=Personnage("ennemi",30)
        if self.niveau == 2:
            joueur=Personnage("joueur",60)
            ennemi=Personnage("ennemi",60)
        if self.niveau == 3:
            joueur=Personnage("joueur",90)
            ennemi=Personnage("ennemi",90)
        
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu! {joueur.nom} remporte la victoire!")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu! {ennemi.nom} remporte la victoire!")
                break
jeu=Jeu()
jeu.lancerJeu()




    

        