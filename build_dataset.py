import os
import json
from ocr_utils import extract_text

# Output dataset file
DATASET_FILE = "dataset.json"

# Root directory containing ML training folders
TRAINING_ROOT = "categorized_bills"

dataset = []

print("\n📦 Building training dataset from categorized folders...")

# Loop through each category folder (Electricity, Grocery, Others, etc.)
for category in os.listdir(TRAINING_ROOT):
    category_path = os.path.join(TRAINING_ROOT, category)

    if not os.path.isdir(category_path):
        continue

    print(f"\n📁 Category: {category}")

    # Loop through each file inside the category folder
    for file_name in os.listdir(category_path):
        file_path = os.path.join(category_path, file_name)

        if not os.path.isfile(file_path):
            continue

        print(f"   🔍 Reading: {file_name}")

        # Extract text using OCR
        text = extract_text(file_path).strip()

        # Skip empty OCR results
        if text == "":
            print("   ⚠️ Skipped (no readable text)")
            continue

        # Add entry to dataset list
        dataset.append({
            "text": text,
            "label": category
        })

# Save dataset file
with open(DATASET_FILE, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4)

print("\n✅ Dataset created successfully!")
print(f"📄 Total samples: {len(dataset)}")
print(f"📌 Saved as: {DATASET_FILE}")
