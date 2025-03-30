import cv2


def resize_image(img, new_dim):
    """new_dim : liste de taille 2"""
    height, width = new_dim[0], new_dim[1]
    rez = cv2.resize(img, (height, width), interpolation=cv2.INTER_CUBIC)
    return rez


def load(filename):
    img = cv2.imread(filename)
    return img
