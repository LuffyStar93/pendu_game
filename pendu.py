
import random
file = open("liste_francais.txt")
allText = file.read()
# print(allText)
words = list(map(str, allText.split()))


# print random string
random_words = random.choice(words)
randomToList = list(random_words)
userWord = []
print('random_words = ', random_words)
# print(randomToList)
compteur = 0 



# function to generate underscore

def underscore(mot):
    r = '_ ' * len(mot)
    userWord = r[:-1].split(' ')
    print('USER WORD =', userWord)
    return userWord

userWord = underscore(randomToList)

while ((compteur <= 7)  or ''.join(userWord) == random_words):
    print(((compteur <= 7)  or ''.join(userWord) == random_words))
    print(''.join(userWord) == random_words)
    print('this is random_word :', random_words)
    print('this is userword :', ''.join(userWord))
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

    display_pendue(compteur)

    # fin de la fonction afficher le pendu

    # fonction pour saisir une lettre

    # def saisie_de_lettre():
    #     lettre = input('Entrez une lettre: ')
    #     if len(lettre) > 1 or ord(lettre) <65 or ord(lettre) > 122:
    #         return saisie_de_lettre()
    #     else:
    #         compteur +1



    # mot = "maison"
    # MOT_TROUVER = ['m', 'a', 'i', 's', 'a', 'n']
    # MOT_TROUVER = list(mot)
    # MOT_USER = ['_', '_', '_', '_', '_', '_']
    # compteur = 0
    lettre_trouver = ''

    # Vérification de la lettre


    def verifLetter(x):
        print('randomword', random_words)
        if x in random_words:
            global lettre_trouver
            lettre_trouver = x
            print('LETTRE_TROUVER DANS VERIFLETTER', lettre_trouver)
            return lettre_trouver
        else:
            global compteur
            compteur += 1
            print('compteur', compteur)


    def add_letter_in_word(mot_1):
        # lettre = input(" ")
        # print('mot1 = ',mot_1)
        INDICE_LIST = []

        for i in range(len(randomToList)):
            # print('random list i', randomToList[i])
            if mot_1 == randomToList[i]:
                INDICE_LIST.append(i)
        print('indice list', INDICE_LIST)
        print('userword', userWord)
        print('randomlist', randomToList)
                

        for i in INDICE_LIST:

            userWord[i] = lettre_trouver

        INDICE_LIST.clear()

    # print(INDICE_LIST)


    verifLetter(input('Choisir une lettre :').lower())
    add_letter_in_word(lettre_trouver)
    # print(lettre_trouver)


    # verifLetter('i')
    # add_letter_in_word(lettre_trouver)
    # print(lettre_trouver)

    # verifLetter('p')
    # verifLetter('h')

    # print(userWord)
    # print(compteur)
    print(' '.join(userWord))
# def verifLettre()
#     if lettre.isalpha() :
#         return lettre.upper()
#     else :
#         return add_letter()