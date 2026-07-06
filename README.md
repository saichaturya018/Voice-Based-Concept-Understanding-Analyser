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
   
🎯 **Workflow**

1. Open the Streamlit application.
2. Upload the student's audio recording.
3. Enter the expected answer.
4. Convert speech to text using Whisper AI.
5. Evaluate the answer using Google Gemini AI.
6. Generate similarity percentage, score, and grade.
7. View AI feedback, strengths, weaknesses, and suggestions.
8. Download the PDF evaluation report.


📸 **Application Screenshots**

1. Home Page
Displays project information and available features.


<img width="1773" height="946" alt="Screenshot 2026-07-06 211412" src="https://github.com/user-attachments/assets/31d2a3f4-fb8a-4713-ad61-4c0b98a00779" />

<img width="1745" height="896" alt="Screenshot 2026-07-06 211423" src="https://github.com/user-attachments/assets/226f413a-3de1-4bec-b00a-71fcaff5f6d2" />


2. Upload Audio
Upload the student's voice recording and provide the expected answer.

 <img width="1847" height="947" alt="Screenshot 2026-07-06 211510" src="https://github.com/user-attachments/assets/2e60653f-4701-4d94-a3f6-4ab8a2b3d992" />


3. AI Analysis
Speech is converted into text using Whisper AI and evaluated using Google Gemini AI.

<img width="1868" height="939" alt="Screenshot 2026-07-06 211603" src="https://github.com/user-attachments/assets/58d447ca-8896-4471-896f-5fbf6c27955a" />

<img width="1733" height="863" alt="Screenshot 2026-07-06 211618" src="https://github.com/user-attachments/assets/8818a52e-ca17-4316-8443-fabf161bbc2b" />


4. Dashboard
Displays the similarity percentage, score, grade, transcript, and AI feedback.

<img width="1814" height="867" alt="Screenshot 2026-07-06 211640" src="https://github.com/user-attachments/assets/4ffc9f3c-8e8a-4c04-a84e-a2214b29ef47" />

<img width="1839" height="946" alt="Screenshot 2026-07-06 211701" src="https://github.com/user-attachments/assets/691b52d6-2fe3-4f97-bc73-c2e853559a63" />



6. PDF Report
Generates a downloadable professional PDF report containing the evaluation.

<img width="1824" height="939" alt="Screenshot 2026-07-06 211724" src="https://github.com/user-attachments/assets/9a6f14e0-653c-4f8f-9fb1-abbe6c5536ce" />

<img width="1920" height="1017" alt="Screenshot 2026-07-06 211734" src="https://github.com/user-attachments/assets/8f1e5471-80c5-4dc5-a537-c3166d826255" />


### Thank you for visiting our repository!

</div>
