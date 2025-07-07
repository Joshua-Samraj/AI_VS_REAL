from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load both models
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL1_PATH = os.path.join(BASE_DIR, 'real_vs_ai_classifier.h5')   # expects 64x64
MODEL2_PATH = os.path.join(BASE_DIR, 'real_vs_ai_classifier2.h5')            # expects 32x32

model1 = tf.keras.models.load_model(MODEL1_PATH)
model2 = tf.keras.models.load_model(MODEL2_PATH)

# Prediction function with size input
def predict_image_with_model(img_path, model, target_size):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    return prediction

def upload_image(request):
    prediction_result_1 = None
    prediction_result_2 = None
    uploaded_image_url = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_instance = form.save()
            image_path = img_instance.image.path

            # Predict using Model 1 (64x64)
            pred1 = predict_image_with_model(image_path, model1, target_size=(64, 64))[0][0]
            prediction_result_1 = "Real" if pred1 > 0.5 else "AI-Generated"

            # Predict using Model 2 (32x32)
            pred2 = predict_image_with_model(image_path, model2, target_size=(32, 32))[0][0]
            prediction_result_2 = "AI-Generated" if pred2 < 0.5 else "Real"  # Adjust this logic to match your model's task

            uploaded_image_url = img_instance.image.url

    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {
        'form': form,
        'prediction1': prediction_result_1,
        'prediction2': prediction_result_2,
        'image_url': uploaded_image_url
    })
