import pickle
import os

MODEL_FILE = "model.pkl"

# Load trained model and vectorizer
if os.path.exists(MODEL_FILE):
    with open(MODEL_FILE, "rb") as f:
        model, vectorizer = pickle.load(f)
else:
    model = None
    vectorizer = None

def predict_category(text):
    """
    Predict category using ML model.
    If ML fails or model not trained, return None.
    """

    if not model or not vectorizer:
        return None

    try:
        X = vectorizer.transform([text])
        pred = model.predict(X)[0]
        return pred
    except:
        return None
