from src.utils.image_processing_operations import load
from src.utils.image_processing_operations import resize_image
import cv2


# Itération 1 : Appliquer un redimensionnement à une image.


def test_resize_image():
    """teste la fonction resize de image_processing_operations à l'aide de la photo mucem.jpg du dossier data_test"""
    img = load("data/data_test/le_puy_en_velay.jpg")
    (h, w, d) = img.shape
    new_dim = (224, 224)
    # when
    resized_image = resize_image(img, new_dim)
    # then
    assert resized_image.shape == (new_dim[0], new_dim[1], d)


if __name__ == "__main__":
    test_resize_image()
