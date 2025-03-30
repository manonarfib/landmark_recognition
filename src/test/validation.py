import tensorflow.keras as keras
from src.create_model import x_test, y_test

# Test modèle entrain

new_model = keras.models.load_model("model_updated.model")

val_loss, val_acc = new_model.evaluate(x_test, y_test)
print(f"Validation loss: {val_loss}, Validation accuracy: {val_acc}")


def test_trained_model():
    new_model = keras.models.load_model("model_updated.model")
    val_loss, val_acc = new_model.evaluate(x_test, y_test)
    print(f"Validation loss: {val_loss}, Validation accuracy: {val_acc}")


if __name__ == "__main__":
    test_trained_model()
