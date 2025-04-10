import openpyxl

def lecture_donnees(file_path='data-folder/data-exemple/exemple.xlsx'):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    # Read n and tau0 from the first two rows
    n = int(sheet.cell(row=1, column=1).value)
    tau0 = float(sheet.cell(row=2, column=1).value) / 100  # Convert percentage to decimal

    # Read investments from rows 3 onward
    placements = []
    row = 3
    while True:
        tauk = sheet.cell(row=row, column=1).value
        dk = sheet.cell(row=row, column=2).value
        fk = sheet.cell(row=row, column=3).value

        if tauk is None or dk is None or fk is None:
            break

        placements.append((float(tauk) / 100, int(dk), int(fk)))
        row += 1

    return n, tau0, placements


def optimiz_coef():
    return


if __name__ == "__main__":
    n, tau0, placements = lecture_donnees('data-folder/data-exemple/exemple.xlsx')

    print("Investment horizon (n):", n)
    print("Base interest rate (tau0):", tau0)
    print("Available investments:")
    for i, (tau, dk, fk) in enumerate(placements, 1):
        print(f"  {i}. Rate: {tau:.4f}, Start: {dk}, End: {fk}")