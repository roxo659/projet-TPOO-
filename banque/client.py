class Client:
    def init(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.comptes = []

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher_comptes(self):
        print(f"\nComptes de {self.nom} :")
        for compte in self.comptes:
            compte.afficher_solde()
