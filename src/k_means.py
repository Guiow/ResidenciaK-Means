import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

data = pd.read_csv('data/X_train.txt', sep='\\s+', header=None)
k_value = 4

# Sabendo que X_train ja esta normalizado
# Redução de dimensionalidade para 2D e 3D
pca_2d = PCA(n_components=2)
X_2d = pca_2d.fit_transform(data)

pca_3d = PCA(n_components=3)
X_3d = pca_3d.fit_transform(data)

# Função para plotar resultados do K-means
def plot_kmeans(X, kmeans, title, dims=2):
    if dims == 0:
        return 0
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    plt.figure(figsize=(8, 6))
    plt.title(title)
    if dims == 2:
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6, edgecolors='k')
        plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X')
        plt.xlabel("PCA Component 1")
        plt.ylabel("PCA Component 2")
    elif dims == 3:
        ax = plt.figure(figsize=(10, 8)).add_subplot(111, projection='3d')
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap='viridis', s=50, alpha=0.6, edgecolors='k')
        ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='red', s=200, marker='X')
        ax.set_xlabel("PCA Component 1")
        ax.set_ylabel("PCA Component 2")
        ax.set_zlabel("PCA Component 3")
        ax.view_init(elev=-30, azim=-75) 
    plt.savefig(f"docs/graphs/clusters{dims}Dk={k_value}")   

# Implementação do K-means para 2 clusters (2D)
kmeans_2d_clusters = KMeans(n_clusters=k_value, random_state=42)
kmeans_2d_clusters.fit(X_2d)
plot_kmeans(X_2d, kmeans_2d_clusters, "K-means Clustering com 2 Clusters (2D)", dims=2)

# Implementação do K-means para 3 clusters (3D)
kmeans_3d_clusters = KMeans(n_clusters=k_value, random_state=42)
kmeans_3d_clusters.fit(X_3d)
plot_kmeans(X_3d, kmeans_3d_clusters, "K-means Clustering com 3 Clusters (3D)", dims=3)

# Avaliação do número de clusters para cada variação
silhouette_2d_2clusters = silhouette_score(X_2d, kmeans_2d_clusters.labels_)
silhouette_3d_3clusters = silhouette_score(X_3d, kmeans_3d_clusters.labels_)

print(f"Silhouette Score ({k_value} Clusters, 2D): {silhouette_2d_2clusters:.3f}")
print(f"Silhouette Score ({k_value} Clusters, 3D): {silhouette_3d_3clusters:.3f}")
