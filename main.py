import os
import re
from ocr_utils import extract_text
from file_organizer import move_file_to_category
from amount_extractor import extract_amount
from date_extractor import extract_date
from text_keyword_extractor import extract_top_keywords

# === For Clustering ===
from cluster_utils import extract_texts, vectorize_texts
from sklearn.cluster import KMeans
from cluster_namer import name_clusters

# ------------------------------
# BILL KEYWORDS
# ------------------------------
BILL_KEYWORDS = ["amount", "total", "subtotal", "rs", "₹",
                 "invoice", "bill", "charges", "payment", "gst"]

def is_bill(text):
    t = text.lower()
    return any(w in t for w in BILL_KEYWORDS)

# ------------------------------
# MAIN PROGRAM STARTS HERE
# ------------------------------
print("\n🚀 Starting Universal Image Classification (OCR + Auto-Clustering)\n")

input_dir = "input_bills"
os.makedirs("categorized_output", exist_ok=True)
summary = {}

# STEP 1 — Load all new images
files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
texts = []
valid_files = []

print("📥 Extracting OCR text from all images...")

for file_name in files:
    file_path = os.path.join(input_dir, file_name)

    # Skip renamed files
    if file_name.startswith("unknown_date_") or re.match(r"\d{4}-\d{2}-\d{2}", file_name):
        continue

    text = extract_text(file_path).strip()
    if text == "":
        print(f"⚠️ Skipped (No text): {file_name}")
        continue

    texts.append(text)
    valid_files.append(file_name)

if len(valid_files) == 0:
    print("\n❌ No new images to process.\n")
    exit()

# -----------------------------------
# STEP 2 — Vectorize for clustering
# -----------------------------------
print("\n🔢 Vectorizing text for clustering...")
X, _ = vectorize_texts(texts)

# Automatic cluster count
num_clusters = min(8, max(2, len(valid_files) // 5))
print(f"🤖 Auto-selected cluster count: {num_clusters}")

# Run KMeans
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(X)

# Auto-generate category names
cluster_names = name_clusters(texts, labels, num_clusters)

print("\n📂 Auto-Generated Folder Names:")
for cid, name in cluster_names.items():
    print(f"  Cluster {cid} → {name}")

# -----------------------------------
# STEP 3 — Process Each File
# -----------------------------------
print("\n⚙ Processing Files One-by-One...\n")

for i, file_name in enumerate(valid_files):
    text = texts[i]
    file_path = os.path.join(input_dir, file_name)

    print(f"\n📄 Processing: {file_name}")

    # 1️⃣ Keyword-based category
    words = extract_top_keywords(text)
    keyword_cat = "_".join(words).title()

    # 2️⃣ If keyword is empty → use cluster category
    if keyword_cat.strip() == "":
        category = cluster_names[labels[i]]
        print(f"✨ Final Category (Cluster): {category}")
    else:
        category = keyword_cat
        print(f"🧠 Final Category (Keywords): {category}")

    # Bill detection + amount
    bill_flag = is_bill(text)
    amount = extract_amount(text) if bill_flag else None

    # Extract date
    date = extract_date(text)

    # Rename file
    new_name = f"{date}_{file_name}"
    new_path = os.path.join(input_dir, new_name)
    if not os.path.exists(new_path):
        os.rename(file_path, new_path)

    # Move file into final folder
    move_file_to_category(new_name, category, base="categorized_output")

    print(f"📦 Moved to: categorized_output/{category}/")

    # Summary for bills
    if bill_flag and amount:
        summary[category] = summary.get(category, 0) + float(amount)

# -----------------------------------
# STEP 4 — Billing Summary
# -----------------------------------
print("\n📊 BILLING SUMMARY:\n")
if len(summary) == 0:
    print("No bills detected.")
else:
    for cat, amt in summary.items():
        print(f"- {cat}: ₹{round(amt, 2)}")

print("\n🎉 DONE — OCR + KEYWORD + K-MEANS CLUSTERING COMPLETED!\n")
