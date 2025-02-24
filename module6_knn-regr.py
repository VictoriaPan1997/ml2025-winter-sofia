import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = None
    
    def fit(self, X, Y):
        self.points = np.column_stack((X, Y))
    
    def predict(self, X_query):
        if self.points is None:
            raise ValueError("Model has not been trained with data.")
        
        distances = np.abs(self.points[:, 0] - X_query)  # Compute absolute distances
        sorted_indices = np.argsort(distances)  # Sort by distance
        k_nearest = self.points[sorted_indices[:self.k]]  # Select k nearest points
        
        return np.mean(k_nearest[:, 1])  # Return mean of k nearest Y values

if __name__ == "__main__":
    try:
        N = int(input("Enter the number of data points (N): "))
        k = int(input("Enter the number of neighbors (k): "))
        
        if k > N:
            raise ValueError("k cannot be greater than N.")
        
        X = np.zeros(N)
        Y = np.zeros(N)
        
        print("Enter the (x, y) points one by one:")
        for i in range(N):
            X[i] = float(input(f"Enter x value for point {i+1}: "))
            Y[i] = float(input(f"Enter y value for point {i+1}: "))
        
        X_query = float(input("Enter the X value to predict Y: "))
        
        knn = KNNRegressor(k)
        knn.fit(X, Y)
        Y_pred = knn.predict(X_query)
        
        print(f"Predicted Y value for X={X_query}: {Y_pred}")
    
    except ValueError as e:
        print(f"Error: {e}")

