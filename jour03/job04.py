class Joueur:
    def __init__(self,nom, numero, position,buts, passes_D,cartons_jaunes,cartons_rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes_D=passes_D
        self.cartons_jaunes=cartons_jaunes
        self.cartons_rouges=cartons_rouges
    def marquerUnBut(self):
        self.buts +=1
    def effectuerUnePasseDecisive(self):
        self.passes_D +=1
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes +=1
    def recevoirUnCartonRouge(self):
        self.cartons_rouges +=1
    def afficherStatistiques(self):
        print(f"Satistiques {self.nom} \nnumero : {self.numero} \nposition: {self.position} \nbut:{ self.buts} \npasses_D :{ self.passes_D} \ncartons_jaunes: {self.cartons_jaunes}\ncartons_rouges : {self.cartons_rouges}")
class Equipe:
    def __init__(self,nom):
        self.nom = nom
        self.liste_joueurs=[]
    def ajouterJoueur(self,joueur):
         self.liste_joueurs.append(joueur)
    def AfficherStatistiquesJoueurs(self): 
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()       
    def mettreAJourStatistiquesJoueur(self,nom, numero, position,buts, passes_D,cartons_jaunes,cartons_rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes_D=passes_D
        self.cartons_jaunes=cartons_jaunes
        self.cartons_rouges=cartons_rouges
ronaldo=Joueur("ronaldo",7,"buteur",0,0,0,0)
messi=Joueur("messi",10,"Ailier droit",0,0,0,0)
giroud=Joueur("Giroud",9,"buteur",0,0,0,0)
om=Equipe("om")
psg=Equipe("psg")
om.ajouterJoueur(ronaldo)
om.ajouterJoueur(messi)
psg.ajouterJoueur(giroud)
om.AfficherStatistiquesJoueurs()
ronaldo.marquerUnBut()
messi.effectuerUnePasseDecisive()
messi.recevoirUnCartonRouge()
ronaldo.recevoirUnCartonJaune()
om.AfficherStatistiquesJoueurs()
    