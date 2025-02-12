# module4.py

# 读取 N（正整数）
N = int(input("Enter a positive integer (N): "))

# 读取 N 个数字
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# 读取 X（整数）
X = int(input("Enter an integer (X): "))

# 查找 X
if X in numbers:
    print(numbers.index(X) + 1)  # 输出索引（从1开始）
else:
    print("-1")  # 没找到


