import argparse


class ShareCalculator:
    def __init__(self):
        self.shares = []
        self.percentages = []
        self.N = 0

    def read_input(self):
        parser = argparse.ArgumentParser(description="Calculate percentage shares.")
        parser.add_argument('N', type=int, help='Number of shares')
        parser.add_argument('shares', type=float, nargs='+', help='List of share values')

        args = parser.parse_args()

        self.N = args.N
        self.shares = args.shares

        if self.N != len(self.shares):
            raise ValueError("Number of shares provided does not match the specified N.")

    def calculate_percentages(self):
        total_shares = sum(self.shares)
        self.percentages = [(share / total_shares) * 100 for share in self.shares]

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
