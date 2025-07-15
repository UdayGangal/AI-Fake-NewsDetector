📰 AI-Powered Fake News Detector

This is an interactive web application built with **Streamlit** and powered by **Google's Gemini API**. It allows users to analyze news articles in real-time to determine their authenticity. If an article is classified as fake, the application can generate a factually accurate, rewritten version.

---

## ✨ Features

- **Real-time Analysis**: Instantly classify any news article as **REAL** or **FAKE**.
- **Truth Meter**: A dynamic chart that visualizes the AI's confidence in its classification.
- **Factual Rewriting**: For articles identified as fake, the AI can generate a corrected, more realistic version.
- **Interactive UI**: A clean and user-friendly interface built with Streamlit.
- **API-Driven**: Powered by Google's Gemini 1.5 Flash API — no local model training required.

---

## 🚀 Demo

 ![fake1](https://github.com/user-attachments/assets/d6f49b72-2422-46d2-b995-ca77d1290795)

![fake 2](https://github.com/user-attachments/assets/94e4ea9c-e6b3-4141-92ea-9e929d8f670c)


---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI Model**: Google Gemini 1.5 Flash API  
- **Dependencies**: `google-generativeai`, `python-dotenv`, `matplotlib`

---

## ⚙️ Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone <https://github.com/UdayGangal/AI-Fake-NewsDetector.git>
cd <AI-Fake-NewsDetector>
```
### 2.Install requirments
```bash
pip install streamlit google-generativeai python-dotenv matplotlib
```
### 3.env File
```bash
GET_YOUR_API_KEY="Your_API_KEY"
```
---

## 📖 How to Use
- **Paste/Type the Article:** *Copy the text of any news article you want to analyze and paste it into the text area.*
- **Analyze: Click the "🔍 Analyze" button:** *The application will send the text to the Gemini API.*
- **View the Result:**  *The "Truth Meter" will update to show the classification (REAL or FAKE) and the confidence score.*
- -**Generate a Real Version:** *If the news is classified as "Fake", a "🛠️ Get the Real News" button will appear. Click it to have the AI generate a factually correct version of the story.*

---
### 📬 Contact

***For any questions, feedback, or collaboration inquiries, feel free to reach out.***
[Uday Gangal](www.linkedin.com/in/uday-gangal-085877347)
