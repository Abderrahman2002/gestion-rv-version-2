class Medecin:
    id_counter = 1  # Variable de classe pour générer automatiquement l'ID
    
    def __init__(self, nom, specialite, adresse, telephone, email,username,password):
        self.nom = nom
        self.specialite = specialite
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.username = username
        self.password = password
        self.id = Medecin.id_counter  # Assigner l'ID automatiquement
        Medecin.id_counter += 1  # Incrémenter l'ID pour le prochain médecin
