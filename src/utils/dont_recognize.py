import numpy as np


def dont_recognize(pred):
    """Entrée : pred = new_model.predict(image)
    avec image qui est un cv2.imread(image_path)

    Sortie : booléen : False si la probabilité 
    que l'image corresponde à un monument de
    la base est inférieure à 0.95
    """
    if np.max(pred) < 0.95:
        return False
    else:
        return True
