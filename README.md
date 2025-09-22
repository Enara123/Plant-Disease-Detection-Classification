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

---

### 📑 Classification Reports

#### **MobileNetV2 (Test Set)**

| Class               | Precision | Recall | F1-Score | Support |
| ------------------- | --------- | ------ | -------- | ------- |
| Apple Scab          | 0.97      | 0.97   | 0.97     | 151     |
| Apple Black Rot     | 0.99      | 1.00   | 0.99     | 149     |
| Apple Healthy       | 0.99      | 0.98   | 0.98     | 150     |
| Potato Early Blight | 1.00      | 0.99   | 0.99     | 145     |
| Potato Late Blight  | 0.96      | 0.91   | 0.94     | 145     |
| Potato Healthy      | 0.95      | 0.99   | 0.97     | 136     |
| Tomato Late Blight  | 0.93      | 0.92   | 0.93     | 138     |
| Tomato Leaf Mold    | 0.95      | 0.99   | 0.97     | 141     |
| Tomato Healthy      | 0.97      | 0.98   | 0.98     | 144     |

**Accuracy:** 0.97 (1299 images)  
**Macro Avg:** Precision 0.97 | Recall 0.97 | F1 0.97  
**Weighted Avg:** Precision 0.97 | Recall 0.97 | F1 0.97

---

#### **ResNet50 (Test Set)**

| Class               | Precision | Recall | F1-Score | Support |
| ------------------- | --------- | ------ | -------- | ------- |
| Apple Scab          | 1.00      | 0.99   | 0.99     | 151     |
| Apple Black Rot     | 0.99      | 1.00   | 0.99     | 149     |
| Apple Healthy       | 1.00      | 1.00   | 1.00     | 150     |
| Potato Early Blight | 1.00      | 1.00   | 1.00     | 145     |
| Potato Late Blight  | 0.98      | 0.99   | 0.99     | 145     |
| Potato Healthy      | 1.00      | 1.00   | 1.00     | 136     |
| Tomato Late Blight  | 0.99      | 0.97   | 0.98     | 138     |
| Tomato Leaf Mold    | 0.99      | 1.00   | 0.99     | 141     |
| Tomato Healthy      | 1.00      | 0.99   | 1.00     | 144     |

**Accuracy:** 0.99 (1299 images)  
**Macro Avg:** Precision 0.99 | Recall 0.99 | F1 0.99  
**Weighted Avg:** Precision 0.99 | Recall 0.99 | F1 0.99

---

### Visualizations

- Streamlit UI
  ![Streamlit UI - Part 1](results/Interface_part2.png)  
   ![Streamlit UI - Part 2](results/Interface_part1.png)

- ResNet50 Confusion Matrix
  ![Confusion Matrix - ResNet50](results/resnet_confusion_matrix.png)

- MobileNetV2 Confusion Matrix
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
