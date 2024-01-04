class CompteBancaire:
    def __init__(self,numDeCompte, nom, prenom, solde,decouvert):
        self.__numDeCompte=numDeCompte
        self.__nom=nom
        self.__prenom=prenom
        self.__solde=solde
        self.__decouvert=decouvert
    def afficher(self): 
        print(f"numéro de compte : {self.__numDeCompte} \n{self.__nom}\n{self.__prenom}\nsolde : {self.__solde}")
    def afficherSolde(self):
        print(f"solde : {self.__solde}")
    def versement(self,versement) :
        self.__solde += versement
        print(f"montant verset: {versement} , solde total : {self.__solde}")
    def retrait(self,retrait): 
        if retrait <= self.__solde:
            self.__solde -= retrait
            print(f"montant retiré: {retrait} , solde total : {self.__solde}")
        else:
            print(f"vous n'avez pas assez de sous sur le compte. Solde : {self.__solde}")
    def agios(self) : 
        if self.__solde < 0:
            self.__solde -= 5

    def virement(self,reference,CompteBancaire,montant):
        reference.afficherSolde()
        CompteBancaire.afficherSolde()
        if montant < CompteBancaire.__solde:
            CompteBancaire.__solde -= montant
            reference.__solde += montant
            print(f"virement éffectué !")
            reference.afficherSolde()
            CompteBancaire.afficherSolde()
        else:
            print("Il n'y a pas assez de sous")

compte1=CompteBancaire(1,"ilyes","chabab",500,True)
compte1.afficher()
compte1.afficherSolde()
compte1.versement(600)
compte1.retrait(500)
compte1.retrait(12000335235)
compte2=CompteBancaire(2,"John","Cena",-50,True)
compte2.virement(compte2,compte1,50)


        

