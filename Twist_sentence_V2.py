from random import randrange

nb = 0
oui = 0
roll1 = 0
roll2 = 0
stop = 0
ad = 0

input("Bonjour est bienvenue dans Twist Sentence, le 1er programme de mixage d'expression française!\nAttention vous êtes sur la 2ème version les expressions ajoutées seront sauvegardées.\nAppuyer sur une touche pour démarrer!")

while stop == 0:
    oui = 0
    while oui != 2 and oui != 1:
        oui = int(input("Ajouter une expression? Taper '1' pour oui et '2' pour non.\n"))

    #Bloc qui ajoute des expréssions aux listes
    if oui == 1:
        print("Combien d'expression voulez vous ajouté ?")
        ad = int(input())
        fichier1 = open('expre1', 'a')
        fichier2 = open("expre2", 'a')
        for i in range(ad): #Nombre d'ajout d'expression
            a = input("Ajouter la 1er partie de l'expression\n") + "\n"
            fichier1.write(a)
            a = input("Ajouter la 2ème partie de l'expression\n") + "\n"
            fichier2.write(a)
        fichier1.close()
        fichier2.close()

        #Bloc qui assemble les bouts d'expressions
    nb = int(input("Combien d'expressions voulez vous ?\n"))
    for i in range(nb):
        fichier1 = open("expre1", "r")
        fichier2 = open("expre2", "r")

        #Bloc qui compte le nombre de ligne des fichiers
        nligne = 0
        for line in fichier1:
            nligne += 1
        fichier1.close()    #On remet le curseur du fichier1 au début pour pouvoir le re-parcourir

        fichier1 = open("expre1", "r")
        roll1 = randrange(nligne)   #On prend deux lignes différentes au hasard
        roll2 = randrange(nligne)
        for i in range(roll1):  #Parcour la liste pour atteindre la ligne = à roll1 ou roll2
            ligne1 = fichier1.readline()    #On met la ligne dans une variable
        for i in range(roll2):
            ligne2 = fichier2.readline()
        print(ligne1 + ligne2)    #On affiche les deux lignes
        fichier1.close()
        fichier2.close()

    stop = int(input("Voulez relancer Twist sentence ?\n(Appuyer sur 1 pour relancer, et un autre chiffre pour quitter.)\n"))
if stop == 418: #Easter eggs
    input("I'm a tea pot \n[error 418]")
else:
    input("Vous allez quitter twist sentence, à bientot !")
