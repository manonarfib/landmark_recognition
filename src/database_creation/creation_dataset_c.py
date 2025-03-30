from detection.detection_landmark import *
import os
from os import listdir
from os.path import isfile, join


# Sous-fonction qui permet de créer les dossiers des bâtiments


def create_folder(ville, batiment):
    """crée les dossiers des batiments dans dataset_c/ville"""
    landmark_folder_path = "dataset_c/" + ville + "/" + batiment
    isExist = os.path.exists(landmark_folder_path)
    if not isExist:  # Create a new directory because it does not exist
        os.makedirs(landmark_folder_path)


# Sous-fonction qui permet de créer un nouveau chemin pour les bâtiments croppés


def new_path(file_path):
    """path vers dossier final des photos cropped et à la bonne taille"""
    path_1 = file_path.split("/")
    name = "dataset_c/" + path_1[1] + "/" + path_1[2] + "/" + path_1[3]
    return name


######################### Fonction qui crée notre base de bâtiments, enregistrée dans dataset_c #############################################


def treatment():
    """- cropper toutes les images du dossier dataset
    - les mettre à la bonne taille 416 x 416
    - les enregistre automatiquement par ville et bâtiment dans dataset_c

    """
    list_cities = [folder for folder in listdir("dataset")]
    # crée une liste avec les noms des villes à partir de celles enregistrées dans dataset

    for city in list_cities:  # ex : "Marseille"

        list_landmarks = [folder for folder in listdir("dataset/" + city)]

        # crée une liste avec les noms des batiments à partir de ceux enregistrés dans le dossier de la ville

        for landmark in list_landmarks:  # ex : Mucem
            create_folder(city, landmark)
            # chemin vers le dossier du bâtiment dans dataset
            landmark_path = "dataset/" + city + "/" + landmark

            list_pictures_names = [
                f for f in listdir(landmark_path) if isfile(join(landmark_path, f))
            ]

            for file in list_pictures_names:  # ex : "00000000.jpg"
                file_path = "dataset/" + city + "/" + landmark + "/" + file

                path_cropped = new_path(file_path)
                isExist = os.path.exists(path_cropped)

                if not isExist:
                    cropped_image = detect_and_cropp(file_path)
                    cv2.imwrite(path_cropped, cropped_image)

            print(landmark)


if __name__ == "__main__":
    treatment()
