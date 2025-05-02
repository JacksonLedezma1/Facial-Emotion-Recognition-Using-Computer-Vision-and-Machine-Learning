# Facial Emotion Recognition

This project uses computer vision and machine learning to detect human faces in images or videos and classify the emotional state expressed (e.g., happy, sad, neutral).

## 🚀 Technologies
- Python 3.8+
- OpenCV
- DeepFace or FER library
- TensorFlow/Keras (optional for custom training)
- FER2013 dataset (Emotion classification)

## 🧠 Emotions Recognized
- Happy
- Sad
- Angry
- Neutral
- Surprise
- Fear
- Disgust

## 📁 Structure
- `src/`: core Python scripts for detection and classification
- `notebooks/`: Jupyter development notebook
- `data/`: data download instructions
- `results/`: output visualizations

## ▶️ Quick Start (Colab or Local)
```bash
pip install -r requirements.txt
python src/classify_emotion.py --input path/to/image.jpg
