import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib
from sklearn.decomposition import PCA

# Load the dataset
df = pd.read_csv('backend/data/all_toyota_data.csv')

# Define relevant columns
required_columns = [
    'City FE (Guide) - Conventional Fuel',
    'Hwy FE (Guide) - Conventional Fuel',
    'Comb FE (Guide) - Conventional Fuel',
    'Comb CO2 Rounded Adjusted - Fuel2',  # May be empty
    'Annual Fuel1 Cost - Conventional Fuel'
]

# Dynamically check for valid columns and exclude empty ones
available_columns = [col for col in required_columns if col in df.columns and df[col].notnull().sum() > 0]

# Select only available columns
features = df[available_columns]

# Handle missing values by replacing NaN with the mean
features = features.fillna(features.mean())

# Normalize the data using StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Determine the optimal number of clusters (Elbow Method)
inertia = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method
plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Train the final K-Means model with optimal clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Save the trained model and scaler for future use
joblib.dump(kmeans, 'backend/models/kmeans_model.joblib')
joblib.dump(scaler, 'backend/models/scaler.joblib')

# Analyze cluster centroids
centroids = kmeans.cluster_centers_
original_centroids = scaler.inverse_transform(centroids)
print("Cluster Centroids (Original Scale):")
print(original_centroids)

# Analyze cluster sizes
print("Cluster Sizes:")
print(df['Cluster'].value_counts())

# Visualize clusters using PCA
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(scaled_features)

plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=df['Cluster'], cmap='viridis', alpha=0.7)
plt.scatter(
    pca.transform(kmeans.cluster_centers_)[:, 0],
    pca.transform(kmeans.cluster_centers_)[:, 1],
    s=300, c='red', marker='X', label='Centroids'
)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('K-Means Clusters (2D)')
plt.legend()
plt.show()
