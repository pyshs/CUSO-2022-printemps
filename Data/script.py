nombre_mots = 0
sortie_fichier = True
phrase = input("Écrivez une phrase: ")
liste_mots = phrase.split(" ")
nombre_mots = len(liste_mots)
nombre_min_lettres = 4
if nombre_mots == 0:
    print("La liste est vide")
else:
    compteur = 0
    for i in liste_mots:
        if len(i) >= nombre_min_lettres:
            compteur+=1
    proportion = round(100*compteur/nombre_mots,2)
    informations = {"Total":compteur,"Proportion":proportion,
                   "Phrase":phrase,"Seuil":nombre_min_lettres}
    sortie = f"Proportion de mots avec {nombre_min_lettres} lettres ou plus : {proportion}"
    print(sortie)
    if sortie_fichier:
        with open("resultat.txt","w") as f:
            f.write(str(informations))