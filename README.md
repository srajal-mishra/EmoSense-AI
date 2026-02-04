# 🎭 EmoSense: Real-Time AI Emotion Detection

**EmoSense** is a computer vision application that detects human emotions in real-time using a webcam feed. Built with a **Python (Flask)** backend for AI processing and a **React.js** frontend for a modern dashboard experience.

---

## 🚀 Features
- **Real-Time Detection:** Instantly identifies emotions (Happy, Sad, Neutral, Angry, Surprise, Fear).
- **Computer Vision:** Powered by **OpenCV** and **DeepFace**.
- **Dual Mode:** - 🖥️ **Desktop Mode:** Runs as a standalone Python window.
  - 🌐 **Web Mode:** Streams video to a React Dashboard.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.x, Flask, OpenCV, DeepFace
- **Frontend:** React.js, Vite
- **AI Model:** DeepFace (pre-trained deep learning models)


## 🧠 How It Works
1. **Face Detection:** The app uses **OpenCV** to locate faces within the webcam's video stream.
2. **AI Analysis:** Each detected face is passed to the **DeepFace** library, which uses deep learning models to analyze facial features.
3. **Emotion Prediction:** The AI predicts the dominant


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/srajal-mishra/EmoSense-AI.git](https://github.com/srajal-mishra/EmoSense-AI.git)
cd EmoSense-AI