# Financial Mathematics Project – Investment Optimization

## 📌 Overview

This project presents an algorithmic solution to the problem of maximizing capital over a discrete time horizon by selecting optimal investment strategies. The investor can use a fixed base rate or various long-term investment products with higher returns. The solution relies on dynamic programming and graph modeling.

---

## 🧠 Mathematical Model

- **Time Horizon:** Discrete period `T = [0, n]`.
- **Base Investment:** Interest rate `τ0` applied to each interval `[t, t+1]`.
- **Specific Investments:** Each product `Pk = (dk, fk, τk)` valid over `[dk, fk]`.

### Graph Representation
- Vertices `V = {0, 1, ..., n}` represent time points.
- Arcs `A` include:
  - `(t, t+1)` with weight `1 + τ0`
  - `(dk, fk)` with weight `1 + τk`

### Objective
Find the **path** `P*` from `0` to `n` in the graph `D` that maximizes:

```
C(P) = Π c(a)   for all a ∈ P
```

### Dynamic Programming Function

Let `Coef(t)` be the maximum capital multiplier up to time `t`:

```
Coef(0) = 1
Coef(1) = (1 + τ0)
Coef(t) = max(
    Coef(t-1) * (1 + τ0),
    max_{k ∈ N⁻(t)} Coef(dk) * (1 + τk)
)
```

Where `N⁻(t)` is the set of all `k` such that `fk = t`.

---

## 📊 Example (n = 7)

### Data

| Product k | Start (`dk`) | End (`fk`) | Interest Rate (`τk`) |
|-----------|--------------|------------|------------------------|
| 1         | 0            | 2          | 1.9%                   |
| 2         | 1            | 3          | 2.0%                   |
| 3         | 2            | 5          | 3.0%                   |
| 4         | 3            | 6          | 3.0%                   |
| 5         | 4            | 7          | 2.8%                   |

### Optimal Strategy
- Optimal path: `0 → 1 → 3 → 6 → 7`
- Final Coefficient: `1.06960`
- This outperforms base-only strategies and mixes specific high-return placements.

---

## ⚙️ Implementation

### Files & Functions

- `data/` – Excel input data.
- `main.py` – Program driver.
- `utils.py`:
  - `lecture_donnees(filepath)` – Reads input from Excel.
  - `optimiz_coef(t, coef, τ0, placements, chemin)` – Computes best Coef(t).
  - `reconstruct_path(chemin, n)` – Backtracks optimal path.

### Algorithm Steps

1. **Read Data** from Excel.
2. **Initialize**: `Coef(0) = 1`, `Coef(1) = 1 + τ0`
3. **Iterate** from `t = 2` to `n` using dynamic programming.
4. **Track** the optimal origin using `chemin`.
5. **Backtrack** final investment path.

---

## 🖥️ How to Run

```bash
pip install openpyxl
python main.py
```

Input Excel file must contain:
- Row 1: `n`, `τ0`
- Rows 2+: `τk dk fk`

---

## 📈 Sample Output

- Capital coefficients: `Coef(0) ... Coef(n)`
- Optimal path: `[start → ... → n]`
- Final multiplier: `Coef(n)`

---

## 🧮 Complexity

- Time complexity: **O(n × m)**  
  (`n`: number of periods, `m`: investment options)

---

## 👨‍🎓 Authors

Erkin Tunc Boya · Rania Seddouki · Nasrallah Layada  
Université Clermont Auvergne – Groupe 13  
Financial Mathematics · Mars–Avril 2025
