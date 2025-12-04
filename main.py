import os
from ocr_utils import extract_text
from file_organizer import move_file_to_category
from amount_extractor import extract_amount
from date_extractor import extract_date
from text_keyword_extractor import extract_top_keywords

# Make sure the output folder exists
os.makedirs("categorized_bills", exist_ok=True)

input_dir = "input_bills"
summary = {}

for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    print(f"\n📄 Processing: {file_name}")

    # Extract OCR text
    text = extract_text(file_path)

    # Extract dynamic keywords (top 2)
    keywords = extract_top_keywords(text)
    category = "_".join(keywords).title()  # e.g. "Apollo_Hospital"

    # Extract amount and date
    amount = extract_amount(text)
    date = extract_date(text)

    # Create final file name: <date>_<originalname>
    new_name = f"{date}_{file_name}"
    new_path = os.path.join(input_dir, new_name)

    # Rename file temporarily
    os.rename(file_path, new_path)

    # Move the file into the new dynamic category folder
    move_file_to_category(new_name, category)

    # Update summary for reporting
    summary[category] = summary.get(category, 0) + amount

    print(f"✔️ Category : {category}")
    print(f"💰 Amount   : ₹{amount}")
    print(f"📅 Date     : {date}")

# Print final summary
print("\n📊 Summary of Total Spent Per Category:")
for category, total in summary.items():
    print(f"- {category}: ₹{round(total, 2)}")
