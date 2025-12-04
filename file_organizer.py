import os
import shutil

def move_file_to_category(file_name, category):
    src = os.path.join("input_bills", file_name)
    
    base_folder = "categorized_bills"
    os.makedirs(base_folder, exist_ok=True)

    category_folder = os.path.join(base_folder, category)
    os.makedirs(category_folder, exist_ok=True)

    dst = os.path.join(category_folder, file_name)
    shutil.move(src, dst)
