import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained models
@st.cache_resource
def load_models():
    resnet_model = tf.keras.models.load_model("resnet_best_model.h5")
    mobilenet_model = tf.keras.models.load_model("moblienet_best_model.h5")
    return resnet_model, mobilenet_model

resnet_model, mobilenet_model = load_models()

# Prediction Diesease Class labels
class_names = [
    'Apple Scab',
    'Apple Black Rot',
    'Apple Healthy',
    'Potato Early blight',
    'Potato Late blight',
    'Potato Healthy',
    'Tomato Late blight',
    'Tomato Leaf Mold',
    'Tomato Healthy'
]

# Preprocessing function
def preprocess_image(image, model_choice):
    img = image.resize((224, 224))
    img_array = np.array(img)

    if model_choice == "ResNet50":
        from tensorflow.keras.applications.resnet50 import preprocess_input
        img_array = preprocess_input(img_array)
    else:  # MobileNetV2 
        img_array = img_array / 255.0  

    img_array = np.expand_dims(img_array, axis=0) 
    return img_array


# Streamlit UI
st.title("🌱 Plant Disease Detection System")
st.write("Upload a leaf image and choose a model to predict the disease.")

# Model selection
model_choice = st.radio("Select Model", ("ResNet50 -> Accuracy: 0.99", "MobileNetV2 -> Accuracy: 0.97"))

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Preprocessing
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

    img_array = preprocess_image(image, model_choice)

    # Model selection
    model = resnet_model if model_choice == "ResNet50" else mobilenet_model

    # Prediction
    preds = model.predict(img_array)[0]
    pred_idx = np.argmax(preds)
    pred_class = class_names[pred_idx]
    confidence = preds[pred_idx]

    # Confidence threshold
    threshold = 0.2
    if confidence >= threshold:
        st.subheader("🔍 Prediction Result")
        st.success(f"Detected Disease: **{pred_class}** ({confidence:.2f})")
    else:
        st.subheader("⚠️ Model is unsure")
        st.warning(f"Highest confidence: {confidence:.2f} — image may not belong to trained classes")

    # Show prediction probabilities
    st.subheader("📊 Prediction Probabilities")
    for cls, prob in zip(class_names, preds):
        st.write(f"- {cls}: **{prob*100:.2f}%**")
