class student:
    def __init__(self,nom,prenom,NumeroEtudiant):
        self.__nom=nom
        self.__prenom=prenom
        self.__NumeroEtudiant=NumeroEtudiant
        self.__Credit=0
        self.__level=self.__studentEval()
    def add_credit(self, credit):
        if credit >0:
            self.__Credit += credit
        else :
            print("Erreur : Le montant est négatif !")
    def NombreCredit(self):
        print(f"Le nombre de crédit de {self.__prenom} {self.__nom} est de {self.__Credit} points")
    def __studentEval(self):
        if self.__Credit >= 90:
            return "Excellent"
        elif self.__Credit >= 80:
            return "Très bien"
        elif self.__Credit >= 70:
            return "Bien"
        elif self.__Credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    def studentInfo(self):
        print(f"Nom : {self.__nom} \nprenom : {self.__prenom} \nId : {self.__NumeroEtudiant} \nNiveau : {self.__studentEval()}")
etudiant1=student("Doe", "John", 145)
etudiant1.add_credit(10)
etudiant1.add_credit(10)
etudiant1.add_credit(10)
etudiant1.NombreCredit()
etudiant1.studentInfo()
    