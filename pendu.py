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
print(random_words)

compteur = 0 
# while compteur <= 5:
