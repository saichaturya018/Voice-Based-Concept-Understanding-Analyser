# 🎙️ Voice-Based Concept Understanding Analyser

> **An AI-powered application that evaluates a user's conceptual understanding through spoken responses using Speech-to-Text, Semantic Analysis, and Audio Feature Extraction.**

---

## 📌 About the Project

The **Voice-Based Concept Understanding Analyser (VBCUA)** is an AI-powered web application developed to assess a user's understanding of concepts through voice input. The application converts speech into text, analyzes semantic similarity between the spoken response and the expected answer, evaluates speech characteristics, and generates an overall performance score along with personalized feedback.

This project is being developed as part of the **APSCHE Google Generative AI Cloud Program**.

---

## ✨ Key Features

- 🎤 Speech-to-Text Conversion
- 🧠 Semantic Understanding & Similarity Analysis
- 🎵 Audio Feature Extraction
- 📊 Intelligent Scoring System
- 📈 Interactive Streamlit Dashboard
- 📄 PDF Report Generation
- 💡 AI-Powered Personalized Feedback

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **Speech Recognition:** OpenAI Whisper
- **Semantic Analysis:** Sentence Transformers / Gemini API
- **Audio Processing:** Librosa
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib
- **Report Generation:** ReportLab
- **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
Voice-Based-Concept-Understanding-Analyser/
│
├── backend/
├── frontend/
├── utils/
├── tests/
├── docs/
├── data/
├── assets/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Project Workflow

```text
User Uploads Audio
        │
        ▼
Speech-to-Text Conversion
        │
        ▼
Semantic Understanding Analysis
        │
        ▼
Audio Feature Extraction
        │
        ▼
Performance Scoring
        │
        ▼
Feedback Generation
        │
        ▼
PDF Report Generation
```

---

## 👨‍💻 Team

| Name | Role |
|------|------|
| Amjuri Sai Chaturya | Team Leader |
| Jami Yuktasri | Member |
| Patnana Mahesh | Member |
| Vayalapalli Maneesha | Member |

---

## 📌 Current Status

🟢 **Project Initialization Completed**

- ✅ Repository Created
- ✅ Folder Structure Initialized
- ✅ Development in Progress

---

## 🚀 Future Enhancements

- Multi-language Speech Support
- Emotion & Sentiment Analysis
- Advanced AI Feedback
- Cloud Deployment
- Performance Analytics Dashboard

---

## 📜 Acknowledgement

This project is developed under the **APSCHE Google Generative AI Cloud Program** as part of a collaborative learning initiative in **Generative AI and Cloud Technologies**.

---

<div align="center">
---

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- FFmpeg installed and added to PATH (required by Whisper for audio decoding)
- Git

### Setup Steps

1. **Clone the repository**
```bash
   git clone https://github.com/saichaturya018/Voice-Based-Concept-Understanding-Analyser.git
   cd Voice-Based-Concept-Understanding-Analyser
```

2. **Create and activate a virtual environment**
```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
```

3. **Install FFmpeg** (required by Whisper)
```bash
   # Windows (using Chocolatey)
   choco install ffmpeg

   # macOS (using Homebrew)
   brew install ffmpeg

   # Linux (Debian/Ubuntu)
   sudo apt update && sudo apt install ffmpeg
```

4. **Install Python dependencies**
```bash
   pip install -r "5. Project Development Phase/requirements.txt"
```

5. **Download NLTK data (first run only)**
```bash
   python -m nltk.downloader punkt stopwords
```

6. **Run the application**
```bash
   streamlit run "5. Project Development Phase/app.py"
```

7. **Open in browser**
   The app will open automatically at `http://localhost:8501`.

### Thank you for visiting our repository!

</div>
