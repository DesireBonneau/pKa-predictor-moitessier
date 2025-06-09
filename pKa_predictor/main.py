# pka_predictor/main.py
import argparse
from .predict import predict

def main():
    parser = argparse.ArgumentParser(description="pKa Predictor CLI")
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV")
    parser.add_argument("--pH", type=float, default=7.4, help="pH value for prediction")
    args = parser.parse_args()

    results = predict(args.input, pH=args.pH)
    # Save or print results:
    print(results)

if __name__ == "__main__":
    main()
