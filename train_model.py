import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

DATASET_FILE = "dataset.json"
MODEL_FILE = "model.pkl"

print("\n📘 Loading dataset...")

# Load dataset
with open(DATASET_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [d["text"] for d in data]
labels = [d["label"] for d in data]

print(f"📄 Total samples: {len(texts)}")
print("📊 Training model...")

# Convert text to TF-IDF numeric vectors
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Save model + vectorizer
with open(MODEL_FILE, "wb") as f:
    pickle.dump((model, vectorizer), f)

print("\n✅ Model trained successfully!")
print(f"💾 Saved as: {MODEL_FILE}")
