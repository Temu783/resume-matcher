import streamlit as st
import pdfplumber
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords if not already
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# -------- Text Cleaning --------
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return " ".join(filtered)

# -------- PDF Text Extractor --------
def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

# -------- Streamlit UI --------
st.set_page_config(page_title="Resume Matcher", page_icon="📄")
st.title("📄 Resume vs Job Description Matcher")

# Upload PDF resume
uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

# Input job description
jd_input = st.text_area("Paste the Job Description here")

if uploaded_resume and jd_input:
    resume_raw = extract_text_from_pdf(uploaded_resume)
    resume_clean = clean_text(resume_raw)
    jd_clean = clean_text(jd_input)

    # TF-IDF + Cosine Similarity
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    match_score = round(score * 100, 2)

    # Keyword matching
    resume_words = set(resume_clean.split())
    jd_words = set(jd_clean.split())
    matched = resume_words & jd_words
    missing = jd_words - resume_words

    # Show results
    st.success(f"📊 Match Score: {match_score}%")
    
    with st.expander("✅ Matched Keywords"):
        st.write(", ".join(sorted(matched)))
    
    with st.expander("❌ Missing Keywords"):
        st.write(", ".join(sorted(missing)))
