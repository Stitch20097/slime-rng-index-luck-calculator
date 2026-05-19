# Slime RNG Index Luck Calculator

A small Windows GUI app for calculating recommended luck values for Slime RNG index slimes.

## How To Use

1. Open `Slime RNG Index Luck Calculator.exe`.
2. Search for a slime or click one in the list.
3. Copy the recommended luck number if you need it.

The calculator rounds luck up to the nearest whole number and adds commas to big numbers.

## Files

- `Slime RNG Index Luck Calculator.py` - main source code
- `Slime RNG Index Luck Calculator.pyw` - no-console launcher for Windows
- `dist/Slime RNG Index Luck Calculator.exe` - built Windows app
- `dist/Slime RNG Index Luck Calculator.zip` - zipped app for sharing

## Build

```powershell
python -m PyInstaller --onefile --windowed --clean --name "Slime RNG Index Luck Calculator" "Slime RNG Index Luck Calculator.py"
```
