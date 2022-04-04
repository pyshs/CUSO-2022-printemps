nombre_min_lettres = 4
sortie_fichier = True
phrase = input("Écrivez une phrase: ")
liste_mots = phrase.split(" ")
nombre_mots = len(liste_mots)
if nombre_mots == 0:
    print("La liste est vide")
else:
    compteur = 0
    for mot in liste_mots:
        if len(mot) >= nombre_min_lettres:
            compteur = compteur + 1
    proportion = 100 * compteur / nombre_mots
    informations = {
        "Total": compteur,
        "Proportion": proportion,
        "Phrase": phrase,
        "Seuil": nombre_min_lettres,
    }
    sortie = f"Proportion de mots avec {nombre_min_lettres} lettres ou plus : {proportion:0.1f}"
    print(sortie)
    if sortie_fichier:
        with open("resultat.txt", "w") as f:
            f.write(str(informations))
