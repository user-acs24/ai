import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib  # For saving and loading the model
import os

class LeaderElectionModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.model_file = "leader_model.pkl"

        # Load the model if it exists
        if os.path.exists(self.model_file):
            self.model = joblib.load(self.model_file)

    def train(self, data, labels):
        """Train the Decision Tree model on the provided data."""
        self.model.fit(data, labels)
        joblib.dump(self.model, self.model_file)  # Save the model after training

    def predict(self, features):
        """Predict the leader node based on the provided features."""
        return self.model.predict(features)

    def update_leader(self, node_metrics):
        """Update the leader based on node metrics."""
        # Prepare the data for prediction (you might want to adjust this based on your actual data)
        features = pd.DataFrame(node_metrics)
        
        # Make predictions
        predictions = self.predict(features)
        
        # Assuming predictions are class labels for leaders
        leaders = [f"Node {pred}" for pred in predictions]
        return leaders

# Example usage (you can remove this or move it to app.py):
if __name__ == "__main__":
    # Sample training data (you should replace this with your actual data)
    # Each row represents a node, columns represent features like CPU usage, memory, etc.
    sample_data = pd.DataFrame({
        'cpu_usage': [20, 30, 50, 70, 90],
        'memory_usage': [30, 20, 10, 50, 60],
        'uptime': [99, 95, 90, 98, 85]
    })
    labels = [0, 1, 0, 1, 0]  # Example labels for nodes (0 or 1 indicating leader)

    model = LeaderElectionModel()
    model.train(sample_data, labels)  # Train the model with the sample data
