from morpion import Morpion

if _name== "_main":
    jeu = Morpion()
    jeu_en_cours = True

    while jeu_en_cours:
        jeu.afficher_plateau()
        print(f"Joueur {jeu.joueur_actuel}, entrez votre coup (ligne et colonne) : ")
        try:
            ligne, colonne = map(int, input().split())

            if jeu.jouer(ligne, colonne):
                if jeu.verifier_victoire():
                    jeu.afficher_plateau()
                    print(f"Le joueur {jeu.joueur_actuel} a gagné !")
                    jeu_en_cours = False
                elif jeu.plateau_rempli():
                    jeu.afficher_plateau()
                    print("Match nul !")
                    jeu_en_cours = False
                else:
                    jeu.changer_joueur()
            else:
                print("Coup invalide, réessayez.")
        except ValueError:
            print("Veuillez entrer deux nombres séparés par un espace.")
