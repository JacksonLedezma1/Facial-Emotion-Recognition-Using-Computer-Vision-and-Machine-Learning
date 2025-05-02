# Facial Emotion Recognition Using Computer Vision and Machine Learning

## 🎯 Objective
Develop a computer vision system that identifies human faces in images or videos and classifies the expressed emotion into basic categories such as happy, neutral, sad, etc.

## 🧠 Description
This project applies facial detection and emotion recognition techniques using public datasets and Python libraries. It aims to demonstrate a practical implementation of machine learning applied to human-computer interaction, safety monitoring, or mental health analysis.

## 🛠️ Tools and Libraries
- `Python 3.x`
- `OpenCV` – for face detection.
- `DeepFace` or `fer` – for facial emotion recognition.
- `Matplotlib` / `Seaborn` – for visualization.
- Dataset: [FER2013](https://www.kaggle.com/datasets/msambare/fer2013)

## 🧪 Project Phases

### 1. Face Detection
- Load image or video using OpenCV.
- Detect faces using Haar Cascades or DeepFace's built-in methods.

### 2. Emotion Classification
**Option 1 (Quick):**
- Use pretrained models from `fer` or `DeepFace`.

**Option 2 (Advanced):**
- Train a CNN on the FER2013 dataset.
- Preprocess images (grayscale, resize to 48x48).
- Evaluate performance with accuracy and confusion matrix.

### 3. Visualization
- Display image with the detected face and emotion label.
- Show emotion statistics across a dataset or video frame-by-frame.

## 📊 Emotion Categories
Based on FER2013 dataset:
- 😠 Angry  
- 🤢 Disgust  
- 😨 Fear  
- 😀 Happy  
- 😢 Sad  
- 😲 Surprise  
- 😐 Neutral

## ✅ Expected Results
- Real-time or image-based facial emotion detection.
- Accuracy report on test data.
- Visual demos using test images or webcam feed. 
