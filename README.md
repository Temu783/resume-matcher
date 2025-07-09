# 📄 Resume vs Job Description Matcher

A simple NLP-based web app built using **Streamlit** to calculate the similarity between a candidate's **Resume (PDF)** and a given **Job Description (text)**.  
It highlights matched skills, missing keywords, and gives a match score using **TF-IDF** and **Cosine Similarity**.

## 🔍 Features

- Upload resume in **PDF**
- Paste job description in **text box**
- Calculates:
  - ✅ Match score (%)
  - ✅ Matched keywords
  - ❌ Missing keywords
- Built using `nltk`, `pdfplumber`, `scikit-learn`, and `streamlit`

## 📸 Screenshot

![screenshot](https://i.imgur.com/urF7J1Y.png) <!-- optional -->

## 🚀 Run it Locally

```bash
# 1. Clone the repo
https://github.com/Temu783/resume-matcher.git
# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Streamlit app
streamlit run app.py
