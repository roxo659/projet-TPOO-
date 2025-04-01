class Banque:
    def init(self, nom):
        self.nom = nom
        self.clients = []

    def ajouter_client(self, client):
        self.clients.append(client)

    def afficher_clients(self):
        print(f"\nClients de la banque {self.nom} :")
        for client in self.clients:
            print(f"- {client.nom} (ID: {client.identifiant})")
