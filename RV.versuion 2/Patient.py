class Patient:
    id_counter = 1  # Variable de classe pour générer automatiquement l'ID
    
    def __init__(self, nom, prenom, age, sexe, adresse, telephone, email,username,password):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.username = username
        self.password = password
        self.id = Patient.id_counter  # Assigner l'ID automatiquement
        Patient.id_counter += 1  # Incrémenter l'ID pour le prochain patient
