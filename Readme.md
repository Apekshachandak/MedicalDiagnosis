# AI-Powered Diagnostic Assistant

## Project Overview

The AI-Powered Diagnostic Assistant is a machine learning-based solution designed to assist healthcare professionals in diagnosing diseases by analyzing medical images like X-rays. This project aims to minimize human error, speed up diagnoses, and improve patient care by providing reliable, data-driven insights.

## Features

- **Medical Image Classification:** Distinguishes between normal and abnormal medical images.
- **Deep Learning Model:** Uses a Convolutional Neural Network (CNN) for image analysis.
- **Web-Based Interface:** React frontend for easy image upload and result viewing.
- **Scalable API:** Flask backend serving model predictions.
- **Data Security:** Ensures patient data privacy through secure API design.

## Project Structure

```
AI-Powered-Diagnostic-Assistant/
|-- backend/
|   |-- dataset/
|   |   |-- normal/
|   |   |-- abnormal/
|   |-- models/
|   |   |-- medical_image_cnn.h5
|   |-- utils/
|   |   |-- image_preprocessing.py
|   |   |-- predict.py
|   |-- app.py
|   |-- config.py
|   |-- requirements.txt
|   |-- train_model.py
|-- frontend/
|   |-- src/
|   |   |-- components/
|   |   |   |-- UploadForm.jsx
|   |   |-- App.jsx
|   |   |-- main.jsx
|   |-- index.html
|-- README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:

```bash
cd backend
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the Flask server:

```bash
python app.py
```

### Frontend Setup

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

## How It Works

- **Image Upload:** User uploads a medical image via the frontend.
- **Preprocessing:** Image is resized and normalized before being passed to the model.
- **Prediction:** The CNN model analyzes the image and returns a diagnosis (Normal/Abnormal) with a confidence score.
- **Result Display:** Results are shown on the frontend.

## Training the Model

1. Ensure your dataset is structured as follows:

```
dataset/
|-- normal/
|-- abnormal/
```

2. Run the training script:

```bash
python backend/train_model.py
```

3. The trained model will be saved in `backend/models/medical_image_cnn.h5`.

## Technologies Used

- Python, Flask
- TensorFlow, Keras
- OpenCV, NumPy
- React, Vite

## Dataset

- ChestX-ray14 Dataset: [https://nihcc.app.box.com/v/ChestXray-NIHCC](https://nihcc.app.box.com/v/ChestXray-NIHCC)

## Contributors

- Apeksha R. Chandak



