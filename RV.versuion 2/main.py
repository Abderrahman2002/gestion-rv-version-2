from Patient import Patient
from Medecin import Medecin
from datetime import datetime
import json

class Menu:
    def __init__(self):
        self.patients = []
        self.medecins = []
        self.medecin_connecte_index = None
        self.load_data()

    def load_data(self):
        try:
            with open("patients.json", "r") as file:
                self.patients = json.load(file)
        except FileNotFoundError:
            self.patients = []

        try:
            with open("medecins.json", "r") as file:
                self.medecins = json.load(file)
        except FileNotFoundError:
            self.medecins = []

    def sauvegarder_donnees(self):
        with open("patients.json", "w") as file:
            json.dump(self.patients, file, indent=4)

        with open("medecins.json", "w") as file:
            json.dump(self.medecins, file, indent=4)

    def afficher_menu(self):
        while True:  # Boucle jusqu'à ce qu'une option valide soit choisie
            print("Menu:")
            print("1. Créer un compte")
            print("2. Se connecter")
            print("3. Déconnexion")
            choix = input("Choisissez une option: ")
            if choix == "1":
                self.creer_compte()
                break  # Sortir de la boucle après avoir exécuté une option valide
            elif choix == "2":
                self.afficher_menu_connexion()
                break  # Sortir de la boucle après avoir exécuté une option valide
            elif choix == "3":
                self.deconnexion()
                break  # Sortir de la boucle après avoir exécuté une option valide
            else:
                print("Option invalide, veuillez choisir à nouveau.")

    def creer_compte(self):
        print("1. Compte Patient")
        print("2. Compte Médecin")
        choix = input("Choisissez une option: ")
        if choix == "1":
            self.creer_compte_patient()
        elif choix == "2":
            self.creer_compte_medecin()
        else:
            print("Option invalide, veuillez choisir à nouveau.")
            self.creer_compte()
    

    def creer_compte_patient(self):
        patient_id = len(self.patients) + 1
        nom = input("Nom du patient: ")
        prenom = input("Prénom du patient: ")
        age = input("Âge du patient: ")
        sexe = input("Sexe du patient: ")
        adresse = input("Adresse du patient: ")
        telephone = input("Téléphone du patient: ")
        email = input("Email du patient: ")
        username = input("Nom d'utilisateur du patient: ")
        password = input("Mot de passe du patient: ")

        patient = {
            "id": patient_id,
            "nom": nom,
            "prenom": prenom,
            "age": age,
            "sexe": sexe,
            "adresse": adresse,
            "telephone": telephone,
            "email": email,
            "username": username,
            "password": password
        }
        self.patients.append(patient)
        print("Compte patient créé avec succès!")
        self.sauvegarder_donnees()
        self.afficher_menu()

    def creer_compte_medecin(self):
        medecin_id = len(self.medecins) + 1
        nom = input("Nom du médecin: ")
        specialite = input("Spécialité du médecin: ")
        adresse = input("Adresse du médecin: ")
        telephone = input("Téléphone du médecin: ")
        email = input("Email du médecin: ")
        username = input("Nom d'utilisateur du médecin: ")
        password = input("Mot de passe du médecin: ")

        medecin = {
            "id": medecin_id,
            "nom": nom,
            "specialite": specialite,
            "adresse": adresse,
            "telephone": telephone,
            "email": email,
            "username": username,
            "password": password
        }
        self.medecins.append(medecin)
        print("Compte médecin créé avec succès!")
        self.sauvegarder_donnees()
        self.afficher_menu()

    def afficher_menu_connexion(self):
        print("Menu de Connexion:")
        print("1. Se connecter en tant que Patient")
        print("2. Se connecter en tant que Médecin")
        choix = input("Choisissez une option: ")
        if choix == "1":
            self.se_connecter_patient()
        elif choix == "2":
            self.se_connecter_medecin()
        else:
            print("Option invalide, veuillez choisir à nouveau.")
            self.afficher_menu_connexion()

    def se_connecter_patient(self):
        print("Se connecter en tant que Patient")
        username = input("Nom d'utilisateur: ")
        password = input("Mot de passe: ")
        for patient in self.patients:
            if patient["username"] == username and patient["password"] == password:
                print("Connexion réussie en tant que patient!")
                self.menu_patient()
                return
        print("Nom d'utilisateur ou mot de passe incorrect.")
        self.afficher_menu()


    def se_connecter_medecin(self):
        print("Se connecter en tant que Médecin")
        username = input("Nom d'utilisateur: ")
        password = input("Mot de passe: ")
        for index, medecin in enumerate(self.medecins):
            if medecin["username"] == username and medecin["password"] == password:
                print("Connexion réussie en tant que médecin!")
                self.medecin_connecte_index = index  # Définir l'index du médecin connecté
                self.menu_medecin()
                return
        print("Nom d'utilisateur ou mot de passe incorrect.")
        self.afficher_menu()

        
    def menu_medecin(self):
        print("Menu Médecin:")
        print("1. Afficher les rendez-vous des patients")
        print("2. Modifier un rendez-vous")
        print("3. Supprimer un rendez-vous")
        print("4. Ajouter un rendez-vous")
        print("5. Déconnexion")

        choix = input("Choisissez une option: ")
        if choix == "1":
            if self.medecin_connecte_index is not None:
                medecin_connecte = self.medecins[self.medecin_connecte_index]
                medecin_id = medecin_connecte["id"]
                print(f"Rendez-vous du médecin {medecin_connecte['nom']} ({medecin_connecte['specialite']}) :")
                rendez_vous = self.charger_rv()  # Charger les rendez-vous
                date = input("Entrez la date des rendez-vous (format YYYY-MM-DD): ")
                rendez_vous_medecin = [rv for rv in rendez_vous if rv["medecin_id"] == str(medecin_id) and rv["date"] == date]
                if rendez_vous_medecin:
                    for rv in rendez_vous_medecin:
                        patient_id = rv["patient_id"]
                        patient = next((pat for pat in self.patients if pat["id"] == int(patient_id)), None)
                        if patient:
                            print(f"Date: {rv['date']}, Heure: {rv['heure']}, ID Patient: {patient['id']}, Nom: {patient['nom']}, Prénom: {patient['prenom']}")
                else:
                    print("Aucun rendez-vous trouvé pour ce médecin à cette date.")
            else:
                print("Aucun médecin n'est connecté.")
        elif choix == "2":
            self.modifier_rv()  # Correction ici
        elif choix == "3":
            self.supprimer_rv()
        elif choix == "4":
            self.ajouter_rv() 
        elif choix == "5":
            self.deconnexion()
        else:
            print("Option invalide, veuillez choisir à nouveau.")
        self.menu_medecin()

            
    def charger_rv(self):
        try:
            with open("rendez_vous.json", "r") as file:
                rendez_vous = json.load(file)
        except FileNotFoundError:
            rendez_vous = []
        return rendez_vous
    
    def modifier_rv(self):
        print("Modification d'un rendez-vous:")
        medecin_id = self.medecins[self.medecin_connecte_index]["id"]
        heure = input("Entrez l'heure du rendez-vous à modifier (format HH:MM): ")
        date = input("Entrez la date du rendez-vous à modifier (format YYYY-MM-DD): ")

        rendez_vous = self.charger_rv()
        rv_a_modifier = None
        for rv in rendez_vous:
            if rv["medecin_id"] == medecin_id and rv["heure"] == heure and rv["date"] == date:
                rv_a_modifier = rv
                break

        if rv_a_modifier:
            nouvelle_heure = input("Entrez la nouvelle heure du rendez-vous (format HH:MM): ")
            nouvelle_date = input("Entrez la nouvelle date du rendez-vous (format YYYY-MM-DD): ")

        # Mettre à jour les informations du rendez-vous
            rv_a_modifier["heure"] = nouvelle_heure
            rv_a_modifier["date"] = nouvelle_date

        # Sauvegarde des modifications dans le fichier JSON
            with open("rendez_vous.json", "w") as file:
                json.dump(rendez_vous, file, indent=4)
        
            print("Rendez-vous modifié avec succès.")
        else:
            print("Aucun rendez-vous trouvé pour cette heure et cette date.")
        self.menu_medecin()
        
        
        
    def supprimer_rv(self):
        print("Suppression d'un rendez-vous:")
        medecin_id = self.medecins[self.medecin_connecte_index]["id"]
        heure = input("Entrez l'heure du rendez-vous à supprimer (format HH:MM): ")
        date = input("Entrez la date du rendez-vous à supprimer (format YYYY-MM-DD): ")

        rendez_vous = self.charger_rv()
        rv_a_supprimer = None
        for rv in rendez_vous:
            if rv["medecin_id"] == medecin_id and rv["heure"] == heure and rv["date"] == date:
                rv_a_supprimer = rv
                break

        if rv_a_supprimer:
            rendez_vous.remove(rv_a_supprimer)
            with open("rendez_vous.json", "w") as file:
                json.dump(rendez_vous, file, indent=4)
            print("Rendez-vous supprimé avec succès.")
        else:
            print("Aucun rendez-vous trouvé pour cette heure et cette date.")

        self.menu_medecin()  # Ajout de cette ligne pour revenir au menu du médecin après la suppression
    


    def deconnexion(self):
        print("Déconnexion réussie.")
        self.afficher_menu()


    def menu_patient(self):
        print("Menu Patient:")
        print("1. Choisir un médecin")
        print("2. Créer un rendez-vous")
        print("3. Choisir un rendez-vous")
        print("4. Déconnexion")
        choix = input("Choisissez une option: ")
        if choix == "1":
            self.choisir_medecin()
        elif choix == "2":
            self.creer_rv()
        elif choix == "3":
            self.choisir_rv()
        elif choix == "4":
            self.deconnexion()
            self.afficher_menu()
        else:
            print("Option invalide, veuillez choisir à nouveau.")
            self.menu_patient()

    def choisir_medecin(self):
        print("Choisir un médecin:")
        if not self.medecins:
            print("Aucun médecin n'est disponible.")
            return
        for medecin in self.medecins:
            print(f"{medecin['id']}. {medecin['nom']}, {medecin['specialite']}")
        self.menu_patient()
        
    def creer_rv(self):
        print("Création d'un rendez-vous:")
        patient_id = input("ID du patient: ")
        medecin_id = input("ID du médecin: ")
        heure = input("Heure du rendez-vous (format HH:MM): ")

        rendez_vous_existant = self.verifier_rv_existant(medecin_id, heure)
        if rendez_vous_existant:
            print("Cette heure est déjà prise pour un rendez-vous.")
        else:
            date = datetime.now().date().strftime('%Y-%m-%d')
            rv = {
                "patient_id": patient_id,
                "medecin_id": medecin_id,
                "heure": heure,
                "date": date,
            }
            print("Rendez-vous créé avec succès!")
            self.ajouter_rv_json(rv)
            self.menu_patient()

    def ajouter_rv_json(self, rv):
        try:
            with open("rendez_vous.json", "r") as file:
                rendez_vous = json.load(file)
        except FileNotFoundError:
            rendez_vous = []

        rendez_vous.append(rv)

        with open("rendez_vous.json", "w") as file:
            json.dump(rendez_vous, file, indent=4)

    def choisir_rv(self):
        print("Choisir un rendez-vous:")
        heure = input("Entrez l'heure du rendez-vous (format HH:MM): ")
        medecin_id = input("Entrez l'ID du médecin: ")

        rendez_vous_existant = self.verifier_rv_existant(medecin_id, heure)
        if rendez_vous_existant:
            print("Désolé, cette heure est déjà prise pour un rendez-vous.")
        else:
            print("Rendez-vous disponible à cette heure.")
        self.menu_patient()

    def verifier_rv_existant(self, medecin_id, heure):
        try:
            with open("rendez_vous.json", "r") as file:
                rendez_vous = json.load(file)
                for rv in rendez_vous:
                    if rv["medecin_id"] == medecin_id and rv["heure"] == heure:
                        return True
        except FileNotFoundError:
            return False

        return False


menu = Menu()
menu.supprimer_rv()
menu.afficher_menu()

