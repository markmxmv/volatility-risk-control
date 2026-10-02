from pathlib import Path

import yfinance as yf


DATA_DIR = Path("data/raw")
OUTPUT_FILE = DATA_DIR / "spy.csv"


def main() -> None:

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    prices = yf.download(
        "SPY",
        interval="1d",
        start="2004-01-01",
        end="2026-01-01",
        auto_adjust=True,
        progress=False,
    )

    if prices.empty:
        raise RuntimeError("No SPY data was downloaded.")

    prices.columns = prices.columns.droplevel(1)

    prices.to_csv(OUTPUT_FILE)

    print(prices.head())
    print()
    print(f"Rows downloaded: {len(prices)}")
    print(f"Date range: {prices.index.min()} — {prices.index.max()}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()