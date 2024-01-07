import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self, nombre_cartes=2):
        main = []
        for _ in range(nombre_cartes):
            carte = self.paquet.pop()
            main.append(carte)
        return main
    def afficher_paquet(self):
            for carte in self.paquet:
                print(carte)


    def calculer_points(self, main):
        total_points = 0
        as_present = False
        for carte in main:
            if carte.valeur.isdigit():
                total_points += int(carte.valeur)
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                total_points += 10
            else:
                as_present = True  # Marque la présence d'un As dans la main
                total_points += 11  # Supposons d'abord que l'As vaut 11 points
        # Si l'As vaut 11 points et le total dépasse 21, alors on compte l'As comme 1 point
        if as_present and total_points > 21:
            total_points -= 10
        return total_points

# Exemple d'utilisation
jeu = Jeu()
jeu.melanger_paquet()

main_joueur = jeu.distribuer_cartes()
main_croupier = jeu.distribuer_cartes()

print("Main du joueur:")
for carte in main_joueur:
    print(f"{carte.valeur} de {carte.couleur}")

print("\nMain du croupier:")
for carte in main_croupier:
    print(f"{carte.valeur} de {carte.couleur}")

total_joueur = jeu.calculer_points(main_joueur)
total_croupier = jeu.calculer_points(main_croupier)

print(f"\nTotal des points du joueur : {total_joueur}")
print(f"Total des points du croupier : {total_croupier}")

    
    