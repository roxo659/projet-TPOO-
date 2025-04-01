from banque import Banque
from client import Client
from compte_bancaire import CompteBancaire

if  _name_ == "main":
    banque = Banque("ABC Bank")

    client1 = Client("Alice", "A123")
    client2 = Client("Bob", "B456")

    compte1 = CompteBancaire("12345", 1000)
    compte2 = CompteBancaire("67890", 500)

    client1.ajouter_compte(compte1)
    client2.ajouter_compte(compte2)

    banque.ajouter_client(client1)
    banque.ajouter_client(client2)

    banque.afficher_clients()
    client1.afficher_comptes()
    client2.afficher_comptes()

    # Transactions
    compte1.deposer(200)
    compte1.retirer(500)
    compte2.retirer(1000)  # Erreur
