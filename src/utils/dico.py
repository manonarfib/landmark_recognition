from os import listdir


def create_dico():
    """Sortie :
    dictionnaire dont les entrées sont les numéros des bâtiments"""

    dico = {}
    list_cities = [f for f in listdir("data/dataset_224") if f != '.DS_Store']
    landmarks = []
    for city in list_cities:
        landmarks.extend([f for f in listdir("data/dataset_224" + "/" + city) if f !='.DS_Store'])
    for i in range(len(landmarks)):
        dico[i] = landmarks[i]

    return dico


def create_dico_cities_landmarks():
    """Sortie :
    dictionnaire  dont les entrées sont les numéros des bâtiments"""

    dico = {}
    landmarks = [
        "Aix-en-Provence, Palais de justice",
        "Aix-en-Provence, Pavillon Noir",
        "Aix-en-Provence, Rotonde",
        "Avignon, Opera",
        "Avignon, Palais des Papes",
        "Avignon, Pont d'Avignon",
        "Tour CMA CGM",
        "Marseille, Chateau d'If",
        "Marseille, Cathedrale La Major",
        "Marseille, Palais Longchamp",
        "Marseille, Mucem",
        "Marseille, Basilique Notre-Dame-de-la-Garde",
        "Marseille, Orange Velodrome",
        "Nice, Monument aux Morts",
        "Nice, Le negresco",
        "Nice, Place Masséna",
        "Nice, Promenade des Anglais",
        "Orange, Arc de Triomphe",
        "Orange, Theatre Antique",
        "Toulon, Bateau Sculpture",
        "Toulon, Fontaine de la Federation",
        "Toulon, Musee de la Marine",
        "Toulon, Le Génie de la Navigation",
    ]
    for i in range(len(landmarks)):
        dico[i] = landmarks[i]

    return dico


def create_dico_1():
    """Sortie :
    dictionnaire dont les entrées sont les noms des bâtiments"""

    dico = {}
    list_cities = [f for f in listdir("data/dataset_224") if f != '.DS_Store']
    landmarks = []
    for ville in list_cities:
        landmarks.extend([f for f in listdir("data/dataset_224" + "/" + ville) if f != '.DS_Store'])
    for i in range(len(landmarks)):
        dico[landmarks[i]] = i

    return dico


if __name__ == "__main__":
    print(create_dico_1())
