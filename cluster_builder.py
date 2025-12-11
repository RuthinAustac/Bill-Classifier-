# cluster_builder.py

import os
from sklearn.cluster import KMeans
from cluster_utils import extract_texts, vectorize_texts
from cluster_namer import name_clusters
from file_organizer import move_file_to_category

def auto_cluster_count(X):
    return 4  # simple fixed number; we can improve later

def build_clusters(input_dir="input_bills"):

    files = [os.path.join(input_dir, f) 
             for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    texts = extract_texts(files)
    X, vectorizer = vectorize_texts(texts)

    n_clusters = auto_cluster_count(X)
    print(f"\n🤖 Auto-selected clusters: {n_clusters}")

    # Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)

    # Generate meaningful category names
    folder_names = name_clusters(texts, labels, n_clusters)
    print("\n📝 Generated Folder Names:")
    for cid, name in folder_names.items():
        print(f"  Cluster {cid} → {name}")

    # Move files into named folders
    for i, file_path in enumerate(files):
        cluster_id = labels[i]
        folder_name = folder_names[cluster_id]

        file_name = os.path.basename(file_path)
        move_file_to_category(file_name, folder_name)

        print(f"📦 {file_name} → {folder_name}/")

    print("\n🎉 Clustering Completed!")

if __name__ == "__main__":
    build_clusters()
