# Financial Mathematics Project – Investment Optimization

This repository contains the implementation of an algorithm to optimize investment policies over a time horizon, based on a mathematical model described in the project PDF.

## Project Description

An investor has multiple investment options, each defined by:
- Start date `dk`
- End date `fk`
- Interest rate `τk`

Additionally, a base interest rate `τ0` applies for all basic periods.

The goal is to determine the best sequence of investments over period `T = [0, n]` to maximize the final capital.

The solution models the problem as a directed graph and uses dynamic programming to compute the optimal path.

## Project Structure

- `data/` - Folder to store investment data files.
- `main.py` - Main Python script implementing the algorithms.
- `utils.py` - Functions for reading data and computing optimal coefficients.
- `README.md` - English project description.
- `README.fr.md` - French project description.

## Requirements

- Python 3.x
- NumPy (optional, for efficiency)

## How to Run

1. Place your data file in the `data/` folder.
2. Run:

```bash
python main.py
```

## The script will output:

- The best investment strategy.
- The maximum final capital achievable.

## Files

- **`lecture_donnees()`**: Reads investment data from the file.
- **`optimiz_coef()`**: Computes the optimal coefficients for each time step.
- **`main()`**: Controls the overall process flow and outputs the results.

