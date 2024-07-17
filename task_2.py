from collections import defaultdict
from typing import List, Tuple


class MegaTrader:
    def __init__(self, N: int, M: int, S: int, lots: List[Tuple[int, str, float, int]]):
        self.N = N
        self.M = M
        self.S = S
        self.lots = lots
        self.lots_details = self._prepare_lots_details()

    def _prepare_lots_details(self) -> List[Tuple[Tuple[int, str, float, int], int, int]]:
        lots_details = []
        for lot in self.lots:
            day, name, price, quantity = lot
            cost = int(price * 10 * quantity)
            profit = quantity * (1000 + 30) - cost
            lots_details.append((lot, profit, cost))
        return lots_details

    def calculate_max_profit(self) -> Tuple[int, List[Tuple[int, str, float, int]]]:
        lots_count = len(self.lots_details)
        dp = [[0] * (self.S + 1) for _ in range(lots_count + 1)]

        for i in range(1, lots_count + 1):
            lot, profit, cost = self.lots_details[i - 1]
            for w in range(self.S + 1):
                if cost <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + profit)
                else:
                    dp[i][w] = dp[i - 1][w]

        w = self.S
        selected_lots = []
        for i in range(lots_count, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                lot, profit, cost = self.lots_details[i - 1]
                selected_lots.append(lot)
                w -= cost

        max_profit = dp[lots_count][self.S]
        return max_profit, selected_lots


def main():
    N, M, S = map(int, input().split())
    day_lots = defaultdict(list)

    while True:
        line = input().strip()
        if not line:
            break
        day, name, price, quantity = line.split()
        day_lots[day].append((int(day), name, float(price), int(quantity)))

    for day, lots in day_lots.items():
        if len(lots) > M:
            raise Exception(f"Incorrect number of lots for day {day}: It should be less than M")

    lots = []
    for l in day_lots.values():
        lots.extend(l)

    trader = MegaTrader(N, M, S, lots)
    profit, selected_lots = trader.calculate_max_profit()

    print(profit)
    for day, name, price, quantity in selected_lots:
        print(f"{day} {name} {price:.1f} {quantity}")


if __name__ == "__main__":
    main()
