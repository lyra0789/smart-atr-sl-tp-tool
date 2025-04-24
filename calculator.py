# calculator.py

import argparse

def calculate_sl_tp(entry_price, atr, rr_ratio=2, direction='long'):
    """
    Calculate Stop-Loss and Take-Profit based on ATR and direction.

    Parameters:
    - entry_price (float)
    - atr (float): Average True Range value
    - rr_ratio (float): Risk-to-Reward ratio
    - direction (str): 'long' or 'short'

    Returns:
    - dict with SL and TP levels
    """
    if direction == 'long':
        sl = entry_price - atr
        tp = entry_price + atr * rr_ratio
    elif direction == 'short':
        sl = entry_price + atr
        tp = entry_price - atr * rr_ratio
    else:
        raise ValueError("Direction must be 'long' or 'short'.")

    return {'Stop-Loss': round(sl, 5), 'Take-Profit': round(tp, 5)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart ATR SL/TP Calculator")
    parser.add_argument("--entry", type=float, required=True, help="Entry price")
    parser.add_argument("--atr", type=float, required=True, help="ATR value")
    parser.add_argument("--rr", type=float, default=2.0, help="Risk-to-Reward ratio")
    parser.add_argument("--dir", type=str, choices=['long', 'short'], default='long', help="Trade direction")

    args = parser.parse_args()
    result = calculate_sl_tp(args.entry, args.atr, args.rr, args.dir)

    print(f"\n📈 Trade Direction: {args.dir.capitalize()}")
    print(f"📍 Entry Price: {args.entry}")
    print(f"📉 Stop-Loss: {result['Stop-Loss']}")
    print(f"📈 Take-Profit: {result['Take-Profit']}\n")
