import os
import cv2
from os import listdir
from os.path import isfile, join


def rename(directory_path):
    """Entrée : chemin vers un répertoire local, chemin absolu

    déplace les images de ce répertoir dans le répertoire data_test, et les renomme"""
    list_images_data_test = [
        f for f in listdir("data/data_test_web") if isfile(join("data/data_test_web", f))
    ]
    list_images_static = [f for f in listdir(
        "static") if isfile(join("static", f))]
    for (
        picture
    ) in (
        list_images_data_test
    ):  # supprime les fichiers déjà présents dans le répertoire d'arrivée
        os.remove("data/data_test_web/" + picture)
    for picture in list_images_static:
        os.remove('static/' + picture)

    list_images = [
        f for f in listdir(directory_path) if isfile(join(directory_path, f))
    ]

    i = 0  # compteur pour renommer les images
    for picture in list_images:  # renomme les fichiers
        image = cv2.imread(directory_path+'/'+picture)
        img = cv2.imwrite('data/data_test_web/'+str(i)+'.jpg', image)
        image_resized = cv2.resize(
            image, (224, 224), interpolation=cv2.INTER_CUBIC)
        img2 = cv2.imwrite('static/'+str(i)+'.jpg', image_resized)
        i += 1


if __name__ == "__main__":
    rename("C:/Users/louis/Documents/codingweeks/images_test")
