class ComteBancaire :
    Compte = {}
    Client = {}
    CompteClient = {}
    nombreCl = 0
    def __init__(self,numCl, mp, solde):
        self.__mp = mp
        self.__solde = solde
        CompteBancaire.nombreClient += 1
        self.__numCl = ComteBancaire.nombreCl
    def getNumCl (self) :
        return self.__numCl
    def getMp (self) :
        return self.__mp
    def getSolde (self) :
        return self.__solde
    def setNumCl (self, numCl) :
        self.__numCl = numCl
    def setMp (self, mp) :
        self.__mp = mp
    def setSolde (self,solde) :
        self.__solde = solde
    # Fonctions
    def ajouterClient(self):
        Client[self.__numCl] = self.__mp
        Compte[self.__numCl] = self.__Solde
        ClientCompte[self.__numCl] = self.__numCl

    def supprimerClient(self):
        del Compte[ClientCompte[self.__numC]]
        del ClientCompte[self.__numC]
        del Client[self.__numC]
    
    def modifierMPClient(self, newMP):
        Client[self.__numCl] = newMP

    def deposer(self, montant):
        Compte[ClientCompte[self.__numCl]] += montant

    def retirer(self, montant):
        if Compte[ClientCompte[self.__numCl]] >= montant:
            Compte[ClientCompte[numCl]] -= montant
        else:
            print("Solde insuffisant.")
            
    import random
    genererNumCompte = lambda numCl: int(str(numCl) + str(random.randint(0, 100)))
    
    import csv
    def ecrireFichierCSV():
        open('clients.csv', 'w', newline='') 
        fieldnames = ['Numéro Client', 'Code Secret']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for numCl, codeSecret in Client.items():
            writer.writerow({'Numéro Client': numCl, 'Code Secret': codeSecret})
            
    def manipSTS():
        numComptesList = list(ClientCompte.values())
        numComptesTuple = tuple(ClientCompte.values())
        numComptesSet = set(ClientCompte.values())

        return numComptesList, numComptesTuple, numComptesSet
    
#main program
print("1. Agent de la banque")
print("2. Client de la banque")
choix = int(input("Entrez votre choix: "))
if choix == 1:
    print("1. Ajouter un compte")
    print("2. Supprimer un compte")
    agent_choix = int(input("Entrez votre choix: "))

    if agent_choix == 1:
        setNumCl(int(input("Entrez le numéro du nouveau client: ")))
        setMp(input("Entrez le code secret du nouveau client: "))
        setNumCl(genererNumCompte(getNumCl()))
        setSolde(float(input("Entrez le solde initial de son compte: ")))
        ajouterClient(getNumCl(), getmp(), getNumC, getSolde)
        print("Compte ajouté avec succès.")
    elif agent_choix == 2:
        setNumCl(int(input("Entrez le numéro du compte à supprimer: ")))
        supprimerClient(grtNumCl)
        print("Compte supprimé avec succès!")
     
elif choix == 2:
    setNumCl(int(input("Entrez votre numéro de client: ")))
    print("1. Modifier le mot de passe")
    print("2. Afficher le solde")
    print("3. Déposer de l'argent")
    print("4. Retirer de l'argent")
    client_choix = int(input("Entrez votre choix: "))

    if client_choix == 1:
        newMP = input("Entrez le nouveau mot de passe: ")
        modifierMPClient(getNumCl(), newMP)
        print("Mot de passe modifié avec succès.")

    elif client_choix == 2:
        print("Solde actuel: ", Compte[ClientCompte[numCl]])

    elif client_choix == 3:
        montant = float(input("Entrez le montant à déposer: "))
        deposer(getNumCl(), montant)
        print("Dépôt effectué avec succès.")

    elif client_choix == 4:
        montant = float(input("Entrez le montant à retirer: "))
        retirer(getNumCl, montant)
        print("Retrait effectué avec succès.")
        






    
        
    

    


    
     


        
    
