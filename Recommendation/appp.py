import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the dataset
data = pd.read_csv('E:/Sem6 Mini Project/ML/Recommendation/freelancer_services.csv')

# Convert categorical variables into numerical values
data['freelancer_id'] = data['freelancer_id'].astype('category').cat.codes
data['service'] = data['service'].astype('category').cat.codes

# Create a dictionary to map numerical indices to service names
service_mapping = dict(enumerate(data['service'].astype('category').cat.categories))

# Split the data into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Calculate item-item similarity matrix
item_similarity = cosine_similarity(train_data[['service', 'client_rating']])

# Function to recommend services to a freelancer
def recommend_services(freelancer_id, n=3):
    # Filter data for the given freelancer
    freelancer_data = test_data[test_data['freelancer_id'] == freelancer_id]
    services_used = set(freelancer_data['service'])
    
    # Calculate average ratings for services used by the freelancer
    avg_ratings = freelancer_data.groupby('service')['client_rating'].mean().to_dict()
    
    recommendations = []
    for service in range(len(item_similarity)):
        if service not in services_used:
            similarity_scores = item_similarity[service]
            sim_sum = 0
            weighted_rating_sum = 0
            for i, sim in enumerate(similarity_scores):
                if i in avg_ratings:
                    sim_sum += sim
                    weighted_rating_sum += sim * avg_ratings[i]
            if sim_sum > 0:
                predicted_rating = weighted_rating_sum / sim_sum
                recommendations.append({'service': service, 'predicted_rating': predicted_rating})
    
    recommendations.sort(key=lambda x: x['predicted_rating'], reverse=True)
    return recommendations[:n]

# Function to map numerical indices to service names
def map_service_names(recommendations):
    for recommendation in recommendations:
        recommendation['service'] = service_mapping[recommendation['service']]

# Example usage
freelancer_id = 0  # Replace 0 with the index of the freelancer_id you want recommendations for
recommended_services = recommend_services(freelancer_id, n=3)
map_service_names(recommended_services)

print(f"Recommended services for freelancer {freelancer_id}:")
for service in recommended_services:
    print(service['service'])
