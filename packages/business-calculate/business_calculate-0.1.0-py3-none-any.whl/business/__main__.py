import business
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="calculate_business")

    parser.add_argument("--revenue", type=float, required=True)
    parser.add_argument("--costs", type=float, required=True)

    args = parser.parse_args()

    business.calculate_profit(args.revenue, args.costs)
    business.calculate_roi(args.revenue, args.costs)