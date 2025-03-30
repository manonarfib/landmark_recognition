from src.check_new_model import check_model_image


def test():
    assert (
        check_model_image("data/data_test/le_puy_en_velay.jpg")
        == "Ce batiment n'est pas dans la base de donnees"
    )
    assert (
        check_model_image("data/dataset_224/Marseille/cma_cgm/00000183.jpg")
        == "The predicted class is cma_cgm"
    )


if __name__ == "__main__":
    test()
