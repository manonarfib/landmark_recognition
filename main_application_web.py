import argparse
import numpy as np
from src.create_model import creation_updated_model
from src.utils.dico import *

from src.utils.dont_recognize import *
import cv2
import os
import tensorflow.keras as keras
from os import listdir
from os.path import join

new_model = keras.models.load_model('model_updated.model')


def main(folder_path):
    """Entrée: 
    chemin vers le dossier contenant les images des bâtiment à identifier

    Sortie: 
    affiche chaque image du dossier source en indiquant le nom du bâtiment, indique si le bâtiment n'est pas dans le base de données"""
    dico_cities_landmarks = create_dico_cities_landmarks()
    dico_dossiers = create_dico()
    list_images = [f for f in listdir(folder_path)]
    res = []
    for picture in list_images:
        img = cv2.imread(folder_path+'/'+picture)
        image_resized = cv2.resize(
            img, (224, 224), interpolation=cv2.INTER_CUBIC)
        image = image_resized.reshape((1, 224, 224, 3))
        pred = new_model.predict(image)
        if dont_recognize(pred) == False:
            res.append("Ce batiment n'est pas dans la base de donnees",)
        else:
            output_class = dico_cities_landmarks[np.argmax(pred)]
            res.append(output_class)
    return res
