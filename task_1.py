import sys


class ShareCalculator:
    def __init__(self):
        self.shares = []
        self.percentages = []
        self.N = 0

    def read_input(self):
        input_data = sys.stdin.read
        data = input_data().split()

        self.N = int(data[0])
        self.shares = list(map(float, data[1:]))

        if self.N != len(self.shares):
            raise ValueError("Number of shares provided does not match the specified N.")

    def calculate_percentages(self):
        total_shares = sum(self.shares)
        self.percentages = [share / total_shares for share in self.shares]

    def print_percentages(self):
        for percentage in self.percentages:
            print(f"{percentage:.3f}")

    def process(self):
        self.read_input()
        self.calculate_percentages()
        self.print_percentages()


if __name__ == "__main__":
    calculator = ShareCalculator()
    calculator.process()
