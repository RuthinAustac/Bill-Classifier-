# cluster_namer.py

import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def clean(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return text

def name_clusters(texts, labels, n_clusters):
    cluster_names = {}

    for cluster_id in range(n_clusters):
        cluster_texts = [clean(texts[i]) for i in range(len(texts)) if labels[i] == cluster_id]

        if len(cluster_texts) == 0:
            cluster_names[cluster_id] = f"Misc_{cluster_id}"
            continue

        vectorizer = TfidfVectorizer(stop_words="english", max_features=5)
        tfidf_matrix = vectorizer.fit_transform(cluster_texts)

        words = vectorizer.get_feature_names_out()

        if len(words) == 0:
            cluster_names[cluster_id] = f"Cluster_{cluster_id}"
        else:
            name = "_".join([w.capitalize() for w in words[:2]])
            cluster_names[cluster_id] = name

    return cluster_names
