import os
from os import listdir
from os.path import isfile, join


def count_images():
    list_cities = [folder for folder in listdir("data/dataset_224")]
    # crée une liste avec les noms des villes à partir de celles enregistrées
    # dans data/dataset_224

    for city in list_cities:  # ex : "Marseille"

        list_landmarks = [folder for folder in listdir("data/dataset_224/" + city)]

        # crée une liste avec les noms des batiments à partir de ceux
        # enregistrés dans le dossier de la ville

        for landmark in list_landmarks:  # ex : Mucem

            landmark_path = "data/dataset_224/" + city + "/" + landmark

            list_pictures_names = [
                f for f in listdir(landmark_path) if isfile(join(landmark_path, f))
            ]

            n = 0

            for file in list_pictures_names:  # ex : "00000000.jpg"

                n += 1

            print(landmark, n)


if __name__ == "__main__":
    count_images()
