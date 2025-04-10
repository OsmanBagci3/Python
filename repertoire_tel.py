# -*- coding: utf-8 -*-

"""Ce programme est une application très basique de répertoire téléphonique"""

import phonenumbers;

print("Bienvenue dans votre répertoire !\n");

user_choice = "";
while user_choice != "0" :
    print("0-quitter\n");
    print("1-écrire dans le répertoire\n");
    print("2-Rechercher dans le répertoire\n");
    print("votre choix?")
    user_choice = input("");
    
    if user_choice != "0" and user_choice != "1" and user_choice != "2" :
        print ("veuillez choisir parmi les options disponibles : \n");
        continue;
    
    if user_choice == "0" :
        print("Fermeture de l'application");
        continue;
    
    if user_choice == "1" :
        saisie_nom = "";
        while saisie_nom != "0" : 
            saisie_nom = input("Nom (0 pour terminer) : ");
            if saisie_nom == "0" : 
                continue;
            else :
                saisie_tel = input("Téléphone : ");
                check_phone_number = phonenumbers.parse(saisie_tel, None);
                while phonenumbers.is_possible_number(check_phone_number) == 'false':
                    print("saisir un format de numéro approprié : +0000000000")    
                    saisie_tel = input("Téléphone : ");
                    check_phone_number = phonenumbers.parse(saisie_tel);
                    
                with open('repertoire.txt', 'a') as f:
                        f.write(saisie_nom + " | ");
                        f.write(saisie_tel + '\n');
    
    if user_choice == "2":
        nom_recherche = input("Entrez un nom : ");
        with open ('repertoire.txt', 'r') as f:
            for l in f.readlines():
                info = l.split(' | ');
                if nom_recherche == info[0] :
                    print(f'Voici le numéro recherché : {info[1]}');
                    break;
            else :
                print("inconnu\n");
                
                    
                
    
