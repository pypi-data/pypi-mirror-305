use std::time::Instant;

use core_rs::types::sheet::XLSXSheet;

fn main() -> anyhow::Result<()> {
    let start = Instant::now();
    let sheet = XLSXSheet::new("A".to_string(), 1, 50, 30);

    for cell in sheet.lock().unwrap().cells() {
        let mut cell = cell.lock().unwrap();

        if cell.row == 5 && cell.column == 5 {
            cell.set_value("AAAAA".to_string())?;
            cell.set_formula("=SUM:A10".to_string())?;
        }
    }

    let cell = sheet.lock().unwrap().find_cell_by_pattern_regex("AAAAA")?;
    println!("Find pattern regex {:?}", cell);

    if let Some(cell) = cell {
        let mut cell = cell.lock().unwrap();
        cell.set_value("BBBBB".to_string())?;
    }

    let cell = sheet.lock().unwrap().find_cell_by_coords(5, 5)?;
    println!("Find Coords {:?}", cell);

    let end = start.elapsed();
    println!(
        "Выполнено за: {}.{:03} сек.",
        end.as_secs(),
        end.subsec_millis(),
    );

    let start = Instant::now();
    let sheet = XLSXSheet::new("A".to_string(), 1, 50, 30);

    for r in 1..=100 {
        for c in 1..=100 {
            let cell = sheet
                .lock()
                .unwrap()
                .write_cell(r, c, &format!("Yop! {}{}", r, c))?;

            let mut guarg_cell = cell.lock().unwrap();
            if guarg_cell.row == 20 && guarg_cell.column == 20 {
                guarg_cell.set_value("AAAAA".to_string())?;
                guarg_cell.set_formula("=SUM(A1:A10)".to_string())?;
            }
        }
    }

    println!(
        "Sheet len cells {:?}",
        sheet.lock().unwrap().cells().collect::<Vec<_>>().len()
    );

    let cell = sheet.lock().unwrap().find_cell_by_coords(1, 1)?;
    println!("Find Coords 1x1 {:?}", cell);

    let cell = sheet.lock().unwrap().find_cell_by_coords(20, 20)?;
    println!("Find Coords 20x20 {:?}", cell);

    let end = start.elapsed();
    println!(
        "Выполнено за: {}.{:03} сек.",
        end.as_secs(),
        end.subsec_millis(),
    );

    Ok(())
}
