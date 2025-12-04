import re
from collections import Counter

# Common words we should ignore
STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "bill", "receipt", "invoice",
    "amount", "total", "date", "no", "id", "address", "order", "txn", "upi",
    "from", "to", "of", "on", "in", "at", "this", "that", "is", "was", "are",
    "a", "an", "as", "by", "etc"
}

def extract_top_keywords(text, top_n=2):
    text = text.lower()

    # Extract words only
    words = re.findall(r"[a-zA-Z]{3,}", text)

    # Remove stopwords
    words = [w for w in words if w not in STOPWORDS]

    if not words:
        return ["Unknown", "File"]

    # Count frequency
    freq = Counter(words).most_common(top_n)

    # Return only the words
    return [word for word, count in freq]
