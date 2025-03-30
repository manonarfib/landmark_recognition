import cv2


def resize(image_path):
    img = cv2.imread(image_path)
    image_resized = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("le_puy_en_velay.jpg", image_resized)


if __name__ == "__main__":
    resize("data/data_test/le-puy-en-velay-2.jpg")
