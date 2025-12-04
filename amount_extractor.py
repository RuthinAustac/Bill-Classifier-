import re

def extract_amount(text):
    # Capture formats like: 123.45, ₹123.45, Rs 123, Rs. 123
    patterns = [
        r"₹\s*\d+\.\d{2}",
        r"rs\.?\s*\d+\.\d{2}",
        r"rs\.?\s*\d+",
        r"\d+\.\d{2}",
        r"\b\d{2,6}\b"  # fallback for whole numbers
    ]

    for pattern in patterns:
        match = re.findall(pattern, text.lower())
        if match:
            value = match[-1]  # last number is usually final amount
            clean = re.sub(r"[^\d.]", "", value)
            try:
                return float(clean)
            except:
                pass
    return 0.0
