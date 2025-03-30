from src.create_model import parsing
import tensorflow.keras as keras
import numpy as np
from src.utils.dico import create_dico
import cv2
import pytest
from src.utils.dont_recognize import *

(x_train, y_train, x_test, y_test) = parsing("data/dataset_224")


new_model = keras.models.load_model("model_updated.model")


dico = create_dico()
print(dico)


def check_model_image(image_path):
    img = img = cv2.imread(image_path)
    image = img.reshape((1, 224, 224, 3))

    # model.predict prend en argument un array de nombres
    pred = new_model.predict(image)
    # print(pred)  # cette ligne permet d'afficher la matrice des probabilités
    if dont_recognize(pred) == False:
        print("Ce batiment n'est pas dans la base de donnees", np.max(pred))
        return "Ce batiment n'est pas dans la base de donnees"
    else:
        output_class = dico[np.argmax(pred)]
        print(output_class, np.max(pred))
        print("The predicted class is", output_class)
        return "The predicted class is " + output_class


if __name__ == "__main__":

    check_model_image("data/dataset_224/Marseille/cma_cgm/00000183.jpg")
    check_model_image("data/dataset_224/Marseille/la_major/00000097.jpg")
    check_model_image("data/dataset_224/Marseille/mucem/00000185.jpg")
    check_model_image("data/dataset_224/Nice/promenade_anglais/00000097.jpg")
    check_model_image("data/dataset_224/Avignon/opera/00000166.jpg")
    check_model_image("data/dataset_224/Orange/theatre_antique/00000317.jpg")
    check_model_image(
        "data/dataset_224/Toulon/fontaine_de_la_federation/00000192.jpg")
    check_model_image("data/dataset_224/Nice/negresco/00000097.jpg")
    check_model_image("data/data_test/le_puy_en_velay.jpg")
