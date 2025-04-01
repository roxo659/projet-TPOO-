class Morpion:
    def init(self):
        self.plateau = [["-" for _ in range(3)] for _ in range(3)]
        self.joueur_actuel = "X"

    def afficher_plateau(self):
        for ligne in self.plateau:
            print(" | ".join(ligne))
        print()

    def jouer(self, ligne, colonne):
        if 0 <= ligne < 3 and 0 <= colonne < 3 and self.plateau[ligne][colonne] == "-":
            self.plateau[ligne][colonne] = self.joueur_actuel
            return True
        return False

    def verifier_victoire(self):
        for i in range(3):
            if self.plateau[i][0] == self.plateau[i][1] == self.plateau[i][2] != "-":
                return True
            if self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] != "-":
                return True
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != "-":
            return True
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != "-":
            return True
        return False

    def plateau_rempli(self):
        return all(cell != "-" for row in self.plateau for cell in row)

    def changer_joueur(self):
        self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"
