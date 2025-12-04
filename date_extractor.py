import re
from datetime import datetime

# Try multiple date formats
DATE_PATTERNS = [
    r"\b\d{2}/\d{2}/\d{4}\b",        # 12/02/2024
    r"\b\d{4}-\d{2}-\d{2}\b",        # 2024-02-12
    r"\b\d{2}-\d{2}-\d{4}\b",        # 12-02-2024
    r"\b\d{1,2}\s+[A-Za-z]{3,}\s+\d{4}\b",   # 12 Jan 2025
    r"\b[A-Za-z]{3,}\s+\d{1,2},\s+\d{4}\b"   # January 5, 2023
]

def extract_date(text):
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, text)
        if match:
            date_str = match.group()
            
            # Try parsing with multiple formats
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%d %b %Y", "%B %d, %Y"):
                try:
                    dt = datetime.strptime(date_str, fmt)
                    return dt.strftime("%Y-%m-%d")  # normalized date
                except:
                    pass
    return "unknown_date"
