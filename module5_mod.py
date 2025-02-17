class NumberProcessor:
    def __init__(self):
        self.numbers = []
    
    def insert_numbers(self, n):
        print(f"Enter {n} numbers:")
        for i in range(n):
            while True:
                try:
                    num = int(input(f"Number {i+1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
    
    def search_number(self, x):
        try:
            index = self.numbers.index(x) + 1  # Convert 0-based index to 1-based
            return index
        except ValueError:
            return -1



