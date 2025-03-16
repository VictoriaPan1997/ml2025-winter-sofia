import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def get_input_pairs(num_pairs, label):
    """Function to read x, y pairs from user input."""
    data = []
    print(f"Enter {num_pairs} (x, y) pairs for {label} set:")
    for _ in range(num_pairs):
        x = float(input("Enter x: "))
        y = int(input("Enter y: "))
        data.append((x, y))
    return np.array(data)

def main():
    # Read training data
    N = int(input("Enter the number of training samples (N): "))
    TrainS = get_input_pairs(N, "training")
    X_train, y_train = TrainS[:, 0].reshape(-1, 1), TrainS[:, 1]
    
    # Read test data
    M = int(input("Enter the number of test samples (M): "))
    TestS = get_input_pairs(M, "test")
    X_test, y_test = TestS[:, 0].reshape(-1, 1), TestS[:, 1]
    
    # Define kNN and perform hyperparameter search using GridSearchCV
    param_grid = {'n_neighbors': list(range(1, 11))}  # k from 1 to 10
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    # Best k value
    best_k = grid_search.best_params_['n_neighbors']
    print(f"Best k: {best_k}")
    
    # Evaluate the best model on the test set
    best_knn = KNeighborsClassifier(n_neighbors=best_k)
    best_knn.fit(X_train, y_train)
    y_pred = best_knn.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Test Accuracy: {test_accuracy:.4f}")

if __name__ == "__main__":
    main()


