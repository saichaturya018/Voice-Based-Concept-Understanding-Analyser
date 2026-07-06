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
🎯 Workflow
1. Open the Streamlit application.
2. Upload the student's audio recording.
3. Enter the expected answer.
4. Convert speech to text using Whisper AI.
5. Evaluate the answer using Google Gemini AI.
6. Generate similarity percentage, score, and grade.
7. View AI feedback, strengths, weaknesses, and suggestions.
8. Download the PDF evaluation report.

📸 Application Screenshots
1. Home Page
Displays project information and available features.
<img width="1920" height="1080" alt="Screenshot 2026-07-06 211412" src="https://github.com/user-attachments/assets/d4dfec62-d5d9-4707-8cbe-826f5d910ca6" />
<img width="1920" height="1080" alt="Screenshot 2026-07-06 211423" src="https://github.com/user-attachments/assets/73df6483-177a-4ad0-b9cc-dde83335d19d" />


2. Upload Audio
Upload the student's voice recording and provide the expected answer. <img width="1920" height="1080" alt="Screenshot 2026-07-06 211510" src="https://github.com/user-attachments/assets/b933640c-ea74-444d-9064-016491afba1c" />

3. AI Analysis
Speech is converted into text using Whisper AI and evaluated using Google Gemini AI.<img width="1920" height="1080" alt="Screenshot 2026-07-06 211603" src="https://github.com/user-attachments/assets/5a0b5abc-692d-4439-9290-0674652f6346" />
<img width="1920" height="1080" alt="Screenshot 2026-07-06 211618" src="https://github.com/user-attachments/assets/a34e2a41-11b6-4eb2-a029-5f5aeceb2296" />

4. Dashboard
Displays the similarity percentage, score, grade, transcript, and AI feedback.<img width="1920" height="1080" alt="Screenshot 2026-07-06 211640" src="https://github.com/user-attachments/assets/90d44e4b-ad71-4761-9f65-880aa7a592c4" />
<img width="1920" height="1080" alt="Screenshot 2026-07-06 211701" src="https://github.com/user-attachments/assets/575692ea-e1d9-47ae-9a9a-9994956ebeb5" />


5. PDF Report
Generates a downloadable professional PDF report containing the evaluation.
<img width="1920" height="1080" alt="Screenshot 2026-07-06 211724" src="https://github.com/user-attachments/assets/e810246f-284f-4e13-8131-3488f6cc32dc" />
<img width="1920" height="1080" alt="Screenshot 2026-07-06 211734" src="https://github.com/user-attachments/assets/00de3d31-f472-42cb-9756-f5d6f4ddbee4" />



### Thank you for visiting our repository!

</div>
