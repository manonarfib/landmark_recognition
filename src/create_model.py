import numpy as np
from os import listdir


import tensorflow.keras as keras
from src.utils.image_processing_operations import load
from keras.layers.core import Dense, Flatten
from tensorflow.keras.models import Sequential
from keras.applications.inception_resnet_v2 import InceptionResNetV2


from src.utils.dico import create_dico_1

dico = create_dico_1()


def creation_landmark_dataset(filename, landmark_index):
    """Entrée :
    chemin d'un répertoire ex : "dataset/Marseille/MUCEM", indice du monument

    Sortie :
    x : liste d'arrays (liste des photos sous forme d'array)
    y : liste de même longueur dont tous les coefficients sont identiques (indice du monument)
    """

    # On crée une liste avec les noms des photos ex "00000000.jpg"

    # on précise != .DS_Store pour éviter les problèmes sur mac
    list_filenames = [f for f in listdir(filename) if f != ".DS_Store"]
    x = []
    y = [landmark_index for i in range(len(list_filenames))]

    for img in list_filenames:
        x.append(load(filename + "/" + img))
    return [x, y]


def parsing_landmark_dataset(x, y):
    """Entrée :
    x : liste d'array de pixels
    y : liste des numéros des monuments correspond à l'array de même indice dans x

    Sortie :
    x_train = liste contenant des arrays de pixels (seulement les 80 % premières images)
    y_train = liste des numéros des monuments correspond à l'array de même indice dans x_train

    x_test : liste contenant des arrays de pixels (les 20 % restant)
    y_test : liste des numéros des monuments correspond à l'array de même indice dans x_test (pour les 20% restant restant)
    """
    n = int(80 * len(x) / 100)
    x_train = x[:n]
    y_train = y[:n]
    x_test = x[n:]
    y_test = y[n:]
    return x_train, y_train, x_test, y_test


def parsing(folder_path):
    """Traitement pour tous les monuments

    Entrée : chemin d'un répertoire ex "dataset_r"

    Sortie :
    x_train = array contenant des arrays de pixels (seulement les 80 % premières images)
    y_train = array contenant les numéros des monuments correspond à l'array de même indice dans x_train

    x_test : array contenant des arrays de pixels (les 20 % restant)
    y_test : array contenant les numéros des monuments correspond à l'array de même indice dans x_test (pour les 20% restant restant)


    """
    list_cities = [f for f in listdir(folder_path) if f != ".DS_Store"]
    landmarks = []

    for city in list_cities:
        list_city_landmark = [f for f in listdir(
            folder_path + "/" + city) if f != ".DS_Store"]
        for i in range(len(list_city_landmark)):
            landmarks.append([city, list_city_landmark[i]])

    # On obtient une liste de type ['Avignon', 'pont_Avignon'], ['Avignon', 'palais_des_papes'], ...]
    # Cette liste permet ultérieurement de reconstituer le chemin vers le
    # dossier du monument

    x_train, y_train, x_test, y_test = [], [], [], []

    for i in range(len(landmarks)):  # On itère sur tous les monuments

        # nom du monument qu'on traite, ex : 'mucem'
        landmark = landmarks[i][1]
        path_to_landmark_folder = (
            folder_path + "/" + landmarks[i][0] + "/" + landmarks[i][1]
        )  # chemin vers le dossier du monument
        landmark_i = dico[landmark]  # indice du monument

        # x_landmark : liste des photos (sous forme d'array), y : liste de même taille dont tous les coeffs sont
        # identiques (numéro d'identification du monument)
        x_landmark, y_landmark = creation_landmark_dataset(
            path_to_landmark_folder, landmark_i
        )

        # On crée des listes avec les 80 premiers % et les 20 derniers %
        (
            x_train_landmark,
            y_train_landmark,
            x_test_landmark,
            y_test_landmark,
        ) = parsing_landmark_dataset(x_landmark, y_landmark)

        # On étend les listes avec les données du monument
        x_train.extend(x_train_landmark)

        y_train.extend(y_train_landmark)
        x_test.extend(x_test_landmark)
        y_test.extend(y_test_landmark)

    return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)


# Variables globales

(x_train, y_train, x_test, y_test) = parsing("data/dataset_224")


def creation_updated_model():
    """

    Returns:
        _type_: _description_
    """
    resnet_model = keras.models.Sequential()

    list_cities = [f for f in listdir("data/dataset_224")if f != ".DS_Store"]
    landmarks = []
    for city in list_cities:
        landmarks.extend(
            [f for f in listdir("data/dataset_224" + "/" + city)if f != ".DS_Store"])
    pretrained_model = InceptionResNetV2(
        include_top=False,
        input_shape=(224, 224, 3),
        pooling="avg",
        classes=len(landmarks),
    )

    # for layer in pretrained_model.layers:
    #    layer.trainable = False

    resnet_model.add(pretrained_model)
    resnet_model.add(Flatten())
    resnet_model.add(Dense(512, activation="relu"))
    resnet_model.add(Dense(len(landmarks), activation="softmax"))

    opt = keras.optimizers.Adam(learning_rate=0.0001)

    resnet_model.compile(
        optimizer=opt,
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    )  # on a changé 'accuracy' en 'sparse_categorical_accuracy'
    resnet_model.fit(x=x_train, y=y_train, epochs=2)
    resnet_model.save("model_updated.model")
    return keras.models.load_model("model_updated.model")


if __name__ == "__main__":
    creation_updated_model()
