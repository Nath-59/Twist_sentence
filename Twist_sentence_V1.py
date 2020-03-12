from random import *

nb = 0
roll1 = 0
roll2 = 0
stop = 1
liste1 = [
"C'est la goutte d'eau,",
"Pierre qui roule",
"c'est l'etincelle",
"A bon entendeur,",
"Ne pas être",
"Ma langue",
"Pas piqué",
"Par monts",
"Ne pas vendre la peau de l'ours",
"La bave du crapaud n'atteint pas",
"L'habit ne fait pas",
"Peigner",
"C'est pas au vieux singe",
"Après l'heure",
"Faire d'une pierre",
"Femme qui rit",
"En avril",
"Sentir",
"L'amour",
"Avoir l'estomac",
"C'est en forgeant",
"Gai comme,",]
liste2 = [
"qui fait déborder le vase",
"n'amasse pas mousse",
"qui met le feu au poudre",
"salut !",
"sorti de l'auberge",
"a fourché",
"des hannetons",
"et par vaux",
"avant de l'avoir tuer",
"la blanche colombe",
"le moine",
"la girafe",
"qu'on apprend a faire des grimace",
"c'est plus l'heure",
"deux coup",
"a moitié dans ton lit",
"ne te découvre pas d'un fil",
"le fagot",
"rend aveugle",
"dans les talons",
"qu'on devient forgeron",
"un pinson",]

input("Bonjour est bienvenue dans Twist Sentence, le 1er programme de mixage d'expression française!\nAttention vous êtes sur la 1er version les expressions ajoutées ne seront pas sauvegardées.\nAppuyer sur une touche pour démarrer!")

#Début de la boucle principale et choix d'ajout d'une expression
while stop == 1:
    oui = 0
    while oui != 2 and oui != 1:
        oui = int(input("Voulez vous ajouter une expression? Taper '1' pour oui et '2' pour non.\n"))

#Bloc d'ajout d'une expression aux listes
    if oui == 1:
        liste1.append(input("Ajouter la 1er partie de l'expression\n"))
        liste2.append(input("Ajouter la 2ème partie de l'expression\n"))

#Bloc de génération des expressions
    nb = int(input("Combien d'expression voulez vous ?\n"))
    for i in range(nb):
        roll1 = randrange(len(liste1))
        roll2 = randrange(len(liste2))
        print(liste1[roll1], liste2[roll2])

#Choix de relancer la boucle principale
    stop = int(input("Voulez relancer Twist sentence ?\n(Appuyer sur 1 pour relancer, et un autre chiffre pour quitter.)\n"))
if stop == 418:
    input("I'm a tea pot \n[error 418]")
else:
    input("Vous allez quitter twist sentence, à bientot !")
