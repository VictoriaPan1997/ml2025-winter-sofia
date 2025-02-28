import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    try:
        # 获取用户输入
        N = int(input("Enter the number of data points (N): "))
        k = int(input("Enter the number of neighbors (k): "))

        if k > N:
            raise ValueError("Error: k cannot be greater than N.")
        
        X = np.zeros((N, 1))  # 存储 X 值
        Y = np.zeros(N)       # 存储 Y 值

        print("Enter the (x, y) points one by one:")
        for i in range(N):
            X[i, 0] = float(input(f"Enter x value for point {i+1}: "))
            Y[i] = float(input(f"Enter y value for point {i+1}: "))

        # 计算 Y 的方差
        variance_y = np.var(Y)
        print(f"Variance of labels (Y): {variance_y:.5f}")

        # 读取要预测的 X 值
        X_query = float(input("Enter the X value to predict Y: "))

        # 训练 k-NN 回归模型
        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(X, Y)
        Y_pred = knn.predict(np.array([[X_query]]))

        print(f"Predicted Y value for X={X_query}: {Y_pred[0]:.5f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

