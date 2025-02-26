import cv2
import numpy as np

def preprocess_image(file):
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (224, 224)) / 255.0
    image = np.expand_dims(image, axis=(0, -1))
    return image