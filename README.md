# 🌱 Plant Disease Detection System

This project is a **deep learning-based system** for detecting plant diseases from leaf images.  
It uses **transfer learning** with pre-trained CNN models to classify apple, potato, and tomato leaves as **healthy** or **diseased**.

---

## 🚀 Features

- Two selectable models: **ResNet50** and **MobileNetV2**
- Upload a leaf image and get real-time disease prediction
- Displays prediction confidence and class probabilities
- Shows overall model test accuracy
- Interactive **Streamlit GUI**

---

## 📂 Dataset

The project uses the [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset), which contains images of healthy and diseased plant leaves.

For this project, **9 classes** were selected:

- **Apple**: Apple Scab, Black Rot, Healthy
- **Potato**: Early Blight, Late Blight, Healthy
- **Tomato**: Late Blight, Leaf Mold, Healthy

---

## 🧠 Models

### 1. ResNet50

- Deep CNN with residual connections
- Achieved **99% accuracy**

### 2. MobileNetV2

- Lightweight CNN optimized for mobile/edge devices
- Achieved **97% accuracy**

---

## 📊 Results

- **ResNet50** → **99% test accuracy**
- **MobileNetV2** → **97% test accuracy**

### Visualizations

![Streamlit UI - Part 1](results/Interface_part1.png)  
![Streamlit UI - Part 2](results/Interface_part2.png)  
![Confusion Matrix - ResNet50](results/resnet_confusion_matrix.png)  
![Confusion Matrix - MobileNetV2](results/moblienet_confusion_matrix.png)

🔗 **Deployed App**: [Plant Disease Detection (Streamlit)](https://plant-disease-detection-classification-kxhhccldyzgfq4yunnqcsv.streamlit.app/)

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/plant-disease-detection.git
cd plant-disease-detection
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---
