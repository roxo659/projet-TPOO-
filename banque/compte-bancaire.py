class CompteBancaire:
    def init(self, numero, solde_initial=0):
        self.numero = numero
        self.solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Montant invalide pour le dépôt.")

    def retirer(self, montant):
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def afficher_solde(self):
        print(f"Compte {self.numero} - Solde : {self.solde}€")
