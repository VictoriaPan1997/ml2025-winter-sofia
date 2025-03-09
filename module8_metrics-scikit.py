import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    try:
        # Read input values
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        X = np.zeros(N, dtype=int)  # Ground truth labels
        Y = np.zeros(N, dtype=int)  # Predicted labels

        print("Enter the (x, y) points one by one:")
        for i in range(N):
            while True:
                try:
                    x = int(input(f"Enter x value for point {i+1} (0 or 1): "))
                    y = int(input(f"Enter y value for point {i+1} (0 or 1): "))
                    if x in [0, 1] and y in [0, 1]:
                        X[i] = x
                        Y[i] = y
                        break
                    else:
                        print("Invalid input. Both x and y must be 0 or 1. Try again.")
                except ValueError:
                    print("Invalid input. Please enter integer values 0 or 1.")

        # Compute Precision and Recall
        precision = precision_score(X, Y, zero_division=0)
        recall = recall_score(X, Y, zero_division=0)

        # Print results
        print("\n=== Results ===")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")

    except ValueError:
        print("Error: Please enter a valid integer for N.")

if __name__ == "__main__":
    main()


