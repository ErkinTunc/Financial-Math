import openpyxl
from utils import lecture_donnees, optimiz_coef, reconstruct_path, enumerate_paths

def main():
    # === Step 1: Load data from Excel ===
    file_path = 'data-folder/data-exemple/exemple.xlsx' # data-folder/Données_groupe_13.xlsx
    n, tau0, placements = lecture_donnees(file_path)

    # === Step 2: Initialize coefficient and path arrays ===
    coef = [0] * (n + 1)
    chemin = [None] * (n + 1)

    coef[0] = 1  # Initial capital
    coef[1] = coef[0] * (1 + tau0)  # First base interest
    chemin[1] = 0

    # === Step 3: Dynamic computation of Coef(t) ===
    for t in range(2, n + 1):
        coef[t] = optimiz_coef(t, coef, tau0, placements, chemin)

    # === Step 4: Reconstruct the optimal investment path ===
    path = reconstruct_path(chemin, n)

    # ==== Step 5: Display all paths === (facultatif)
    # enumerate_paths(n, tau0, placements)

    # === Step 6: Display optimal path ===
    print("\nOptimal capital coefficients:")
    for t in range(n + 1):
        print(f"Coef({t}) = {coef[t]:.5f}")

    print("\nOptimal path (from -> to):")
    for step in path:
        print(f"{step[0]} -> {step[1]}")

    print(f"\nFinal capital coefficient: {coef[n]:.5f}")

if __name__ == "__main__":
    main()