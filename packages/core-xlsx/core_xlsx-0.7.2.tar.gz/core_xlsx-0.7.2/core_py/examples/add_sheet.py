from core_xlsx import XLSXSheet
import time


if __name__ == "__main__":
    start_time = time.time()

    sheet = XLSXSheet("A", 1)
    print("Sheet", sheet)

    print("Write Cell 100x100")
    cell = sheet.write_cell(100, 100, "Жопа")

    cell.set_formula("SUM(A1:A10)")
    cell.set_style_id("Style: Percent")

    cell = sheet.find_cell_by_coords(100, 100)
    print(
        "Find Cell 100x100 value:",
        cell.value if cell else cell,
        "formula:",
        cell.formula if cell else cell,
        "StyleID:",
        cell.style_id if cell else cell,
    )

    for cell in sheet.cells:
        if cell.row == 99 and cell.column == 99:
            cell.set_value("Yop! Жопа")
            cell.set_style_id("Style Yop! Жопа")

    cell = sheet.find_cell_by_coords(99, 99)
    print(
        "Find Cell 99x99 value:",
        cell.value if cell else cell,
        "StyleID:",
        cell.style_id if cell else cell,
    )

    print(f"Выполнено за: {time.time() - start_time:.3f} сек.")
