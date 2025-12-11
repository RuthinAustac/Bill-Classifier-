# main_cluster.py
import os
from cluster_builder import build_clusters
from cluster_namer import name_clusters
from file_organizer import move_file_to_category

os.makedirs("categorized_clusters", exist_ok=True)

print("\n🤖 Starting AUTO-CLUSTERING (OCR + Unsupervised ML)\n")

files, texts, labels = build_clusters("input_bills")

cluster_names = name_clusters(texts, labels)

print("\n📂 Final Cluster Names:")
for c, name in cluster_names.items():
    print(f"Cluster {c}: {name}")

for i, file_path in enumerate(files):
    file_name = os.path.basename(file_path)
    cluster_id = labels[i]
    folder_name = cluster_names[cluster_id]

    move_file_to_category(file_name, folder_name, base="categorized_clusters")

    print(f"📦 {file_name} → {folder_name}")

print("\n🎉 AUTO-CLUSTERING COMPLETE!")
