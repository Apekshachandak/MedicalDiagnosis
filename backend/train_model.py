import os
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report

# Paths
DATASET_DIR = 'dataset/'
IMAGE_SIZE = (224, 224)

# Load and preprocess dataset
def load_data():
    images, labels = [], []
    for label, category in enumerate(['normal', 'abnormal']):
        category_dir = os.path.join(DATASET_DIR, category)
        for file in os.listdir(category_dir):
            img_path = os.path.join(category_dir, file)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, IMAGE_SIZE) / 255.0
            images.append(image)
            labels.append(label)
    images = np.expand_dims(np.array(images), axis=-1)
    labels = np.array(labels)
    return train_test_split(images, labels, test_size=0.2, random_state=42)

# Build the CNN model
def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(256, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Train the model
def train_model():
    X_train, X_test, y_train, y_test = load_data()
    model = build_model()

    class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
    class_weights = dict(enumerate(class_weights))

    datagen = ImageDataGenerator(
        rotation_range=15,
        zoom_range=0.2,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )

    model.fit(datagen.flow(X_train, y_train, batch_size=32),
              epochs=10,
              validation_data=(X_test, y_test),
              class_weight=class_weights)

    y_pred = (model.predict(X_test) > 0.5).astype('int32')
    print(classification_report(y_test, y_pred))

    model.save('models/medical_image_cnn.h5')
    print('Model trained and saved successfully!')

if __name__ == '__main__':
    train_model()