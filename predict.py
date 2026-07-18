import numpy as np
from PIL import Image
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("model.keras")

# CIFAR-10 class names
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((32, 32))

    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)

    predicted_class = np.argmax(prediction)
    confidence = float(np.max(prediction) * 100)

    return class_names[predicted_class], confidence