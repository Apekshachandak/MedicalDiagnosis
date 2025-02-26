from tensorflow.keras.models import load_model
from utils.image_preprocessing import preprocess_image

model = load_model('models/medical_image_cnn.h5')

def predict_image(file):
    image = preprocess_image(file)
    prediction = model.predict(image)
    diagnosis = 'Normal' if prediction[0][0] > 0.5 else 'Abnormal'
    return {'diagnosis': diagnosis, 'confidence': float(prediction[0][0])}