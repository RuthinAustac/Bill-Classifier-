# cluster_utils.py
from ocr_utils import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_texts(image_files):
    texts = []
    for f in image_files:
        text = extract_text(f).strip()
        texts.append(text)
    return texts

def vectorize_texts(texts):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(texts)
    return X, vectorizer
