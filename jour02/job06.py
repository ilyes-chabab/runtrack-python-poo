class commande:
    def __init__(self,numeroDeCommande,):
        self.__numeroDeCommande= numeroDeCommande
        self.__listeDePlatsCommandes={}
        self.__statutDeLaCommande="en cours"
    def ajouterPlat(self,plat,prix):
        self.__listeDePlatsCommandes[plat] = {"prix": prix, "statut": "En cours"}
        print(f"{plat} ajouté à la commande.")
    def annulerCommande(self):
        self.__statutDeLaCommande="annulée"
        print("la commande a été annulée")
    def __totalPrix(self):
        total = 0
        for plat, info in self.__listeDePlatsCommandes.items():
            total += info["prix"]
        return total
    def calculerTVA(self):
        total = self.__totalPrix()
        tva=0.2*total
        return tva
    def infoCommande(self):
        print(f"\nLa commande numéro {self.__numeroDeCommande} : ")
        for plat , info in self.__listeDePlatsCommandes.items():
            print(f"{plat} : {info['prix']} € {info['statut']}")
        total= self.__totalPrix()
        print(f"Total à payer : {total} ({self.calculerTVA()}€ de TVA incluse)")
    

cmd1=commande(1)
cmd1.ajouterPlat("pizza",8)
cmd1.ajouterPlat("langouste",18)
cmd1.ajouterPlat("caviar",54)
cmd1.infoCommande()


        

