#     ==========Y===
#    ||  /      |
#    || /       |
#    ||/        O
#    ||        /|\
#    ||        /|
#    ||
#   /||
#  //||
# ============




import random
file = open("liste_francais.txt")
allText = file.read()
# print(allText)
words = list(map(str, allText.split()))


# print random string
random_words = random.choice(words)
randomToList = list(random_words)
userWord = []
print(randomToList)

compteur = 0 
# while compteur <= 7:


# function to generate underscore
# def underscore(mot):
#     r = '_ ' * len(mot)
#     print(r[:-1])
#     return r[:-1]

# underscore(randomToList)

# fonction pour afficher le pendu
potence = []

potence.append('     ==========Y===')
potence.append('    ||  /      |')
potence.append('    || /       |')
potence.append('    ||/        O')
potence.append('    ||        /|\\')
potence.append('    ||        / \\')
potence.append('    ||\n'
               '   /||\n'
               '  //||\n'
               '============')


def display_pendue(nb):
    for e in range(nb):
        print(potence[e])

# display_pendue(compteur)

# fin de la fonction afficher le pendu

# fonction pour saisir une lettre

# def saisie_de_lettre():
#     lettre = input('Entrez une lettre: ')
#     if len(lettre) > 1 or ord(lettre) <65 or ord(lettre) > 122:
#         return saisie_de_lettre()
#     else:
#         compteur +1