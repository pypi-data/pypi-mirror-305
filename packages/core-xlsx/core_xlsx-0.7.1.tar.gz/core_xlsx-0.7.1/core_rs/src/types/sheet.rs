use std::{
    collections::HashMap,
    sync::{Arc, Mutex},
};

use anyhow::{bail, Result};
use rayon::prelude::*;

use super::{cell::XLSXSheetCell, MAX_COL, MAX_ROW};

#[derive(Clone, Debug, Default)]
pub struct XLSXSheet {
    pub name: String,
    pub max_row: u32,
    pub max_column: u16,
    pub index: i32,
    // todo
    pub _cells: HashMap<(u32, u16), Arc<Mutex<XLSXSheetCell>>>,
    // _current_workbook: Weak<Mutex<XLSXBook>>,
}

impl XLSXSheet {
    pub fn new(name: String, index: i32, rows: u32, cols: u16) -> Arc<Mutex<Self>> {
        if rows > MAX_ROW || cols > MAX_COL {
            panic!("Row or Column is out of range");
        }

        // Создаем лист
        let sheet = Arc::new(Mutex::new(Self {
            name,
            max_row: rows,
            max_column: cols,
            index,
            ..Default::default()
        }));

        // Создаем список ячеек по умолчанию
        let cells: HashMap<_, _> = (1..=rows)
            .into_par_iter()
            .flat_map(|r| {
                let sheet = Arc::clone(&sheet);
                (1..=cols).into_par_iter().map(move |c| {
                    let cell = XLSXSheetCell::new(Arc::clone(&sheet), r, c, None);
                    ((r, c), cell)
                })
            })
            .collect();

        // Заполняем список ячеек
        sheet.lock().unwrap()._cells = cells;

        sheet
    }

    pub fn cells(&self) -> impl Iterator<Item = &Arc<Mutex<XLSXSheetCell>>> {
        let mut cells = self._cells.values().collect::<Vec<_>>();
        cells.sort_by_key(|k| {
            let cell = k.lock().unwrap();
            (cell.row, cell.column)
        });

        cells.into_iter()
    }

    pub fn iter_cells(
        &self,
        min_row: Option<u32>,
        max_row: Option<u32>,
        min_col: Option<u16>,
        max_col: Option<u16>,
    ) -> Result<impl Iterator<Item = &Arc<Mutex<XLSXSheetCell>>>> {
        let min_row = min_row.unwrap_or(1);
        let max_row = max_row.unwrap_or(self.max_row);
        let min_col = min_col.unwrap_or(1);
        let max_col = max_col.unwrap_or(self.max_column);

        if min_row > max_row || min_col > max_col {
            bail!("The coordinates of the cells were incorrectly transmitted");
        }

        let cells = self
            ._cells
            .par_iter()
            .filter(move |(_, cell)| {
                let cell = cell.lock().unwrap();
                cell.row >= min_row
                    && cell.row <= max_row
                    && cell.column >= min_col
                    && cell.column <= max_col
            })
            .map(|(_, cell)| cell)
            .collect::<Vec<_>>()
            .into_iter();

        Ok(cells)
    }

    pub fn find_cells_by_pattern_regex(
        &self,
        pattern: &str,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        // Создаем регулярное выражение
        let re = regex::Regex::new(pattern)?;

        let cells = self
            ._cells
            .par_iter()
            .filter_map(|(_, cell)| {
                let cell_guard = cell.lock().unwrap();
                if re.is_match(&cell_guard.value.get_value_str()) {
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    pub fn find_cells_for_rows_pattern_regex(
        &self,
        pattern: &str,
        col_stop: Option<u16>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        // Создаем регулярное выражение
        let re = regex::Regex::new(pattern)?;

        let cells = self
            ._cells
            .par_iter()
            .filter_map(|(_, cell)| {
                let cell_guard = cell.lock().unwrap();
                if re.is_match(&cell_guard.value.get_value_str()) {
                    if let Some(col_stop) = col_stop {
                        if cell_guard.column >= col_stop {
                            return None;
                        }
                    }
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    pub fn find_cells_for_cols_pattern_regex(
        &self,
        pattern: &str,
        row_stop: Option<u32>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        // Создаем регулярное выражение
        let re = regex::Regex::new(pattern)?;

        let cells = self
            ._cells
            .par_iter()
            .filter_map(|(_, cell)| {
                let cell_guard = cell.lock().unwrap();
                if re.is_match(&cell_guard.value.get_value_str()) {
                    if let Some(row_stop) = row_stop {
                        if cell_guard.row >= row_stop {
                            return None;
                        }
                    }
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    pub fn find_cells_multi_pattern_regex(
        &self,
        pattern_1: &str,
        pattern_2: &str,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re1 = regex::Regex::new(pattern_1).unwrap();
        let re2 = regex::Regex::new(pattern_2).unwrap();

        let cells = self
            ._cells
            .par_iter()
            .filter_map(|(_, cell)| {
                let cell_guard = cell.lock().unwrap();
                if re1.is_match(&cell_guard.value.get_value_str())
                    || re2.is_match(&cell_guard.value.get_value_str())
                {
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    pub fn find_cells_between_patterns(
        &self,
        pattern_start: &str,
        pattern_end: &str,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re_start = regex::Regex::new(pattern_start)?;
        let re_end = regex::Regex::new(pattern_end)?;

        let mut cells = Vec::new();
        let mut capturing = false;

        for (_, cell) in self._cells.iter() {
            let cell_guard = cell.lock().unwrap();
            let val = cell_guard.value.get_value_str();

            if re_start.is_match(&val) {
                capturing = true;
                continue;
            }

            if re_end.is_match(&val) {
                capturing = false;
            }

            if capturing {
                cells.push(Arc::clone(cell));
            }
        }

        Ok(cells)
    }

    pub fn find_cells_by_range_rows(
        &self,
        start_row: u32,
        end_row: u32,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let cells = self
            ._cells
            .par_iter()
            .filter_map(|(_, cell)| {
                let cell_guard = cell.lock().unwrap();
                if cell_guard.row >= start_row && cell_guard.row <= end_row {
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    pub fn find_cells_by_range_cols(
        &self,
        start_col: u16,
        end_col: u16,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let cells = self
            ._cells
            .par_iter()
            .filter_map(|(_, cell)| {
                let cell_guard = cell.lock().unwrap();
                if cell_guard.column >= start_col && cell_guard.column <= end_col {
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    pub fn find_cell_by_coords(
        &self,
        row: u32,
        col: u16,
    ) -> Result<Option<Arc<Mutex<XLSXSheetCell>>>> {
        let cell = self._cells.get(&(row, col));
        Ok(cell.cloned())
    }

    pub fn find_cell_by_pattern_regex(
        &self,
        pattern: &str,
    ) -> Result<Option<Arc<Mutex<XLSXSheetCell>>>> {
        let re = regex::Regex::new(pattern)?;
        let cell = self._cells.par_iter().find_map_first(|(_, cell)| {
            let cell_guard = cell.lock().unwrap();
            if re.is_match(&cell_guard.value.get_value_str()) {
                Some(Arc::clone(cell))
            } else {
                None
            }
        });
        Ok(cell)
    }

    pub fn find_cell_by_cell(&self, cell: &str) -> Result<Option<Arc<Mutex<XLSXSheetCell>>>> {
        let found_cell = self._cells.par_iter().find_map_first(|(_, c)| {
            if c.lock().unwrap().cell == cell {
                Some(Arc::clone(c))
            } else {
                None
            }
        });

        Ok(found_cell)
    }

    pub fn write_cell(
        &mut self,
        row: u32,
        col: u16,
        value: &str,
    ) -> Result<Arc<Mutex<XLSXSheetCell>>> {
        if row > MAX_ROW || col > MAX_COL {
            bail!("Row or Column is out of range");
        }

        if row < 1 || col < 1 {
            bail!("Row and Column must be greater than 0");
        }

        if let Some(cell) = self._cells.get_mut(&(row, col)) {
            let mut cell_guard = cell.lock().unwrap();
            cell_guard.set_value(value.to_string())?;

            Ok(cell.clone())
        } else {
            // Добавление ячейки в список ячеек
            let current_sheet = Arc::new(Mutex::new(self.clone()));
            let cell = XLSXSheetCell::new(
                Arc::clone(&current_sheet),
                row,
                col,
                Some(value.to_string()),
            );

            self._cells.insert((row, col), Arc::clone(&cell));

            let mr = row as i32 - self.max_row as i32;
            let mc = col as i32 - self.max_column as i32;

            // TODO
            if mr > 1 || mc > 1 {
                // Создаем новые ячейки которые не существуют
                let cells: HashMap<_, _> = (1..=row)
                    .into_par_iter()
                    .flat_map(|r| {
                        let current_sheet = Arc::clone(&current_sheet);
                        (1..=col).into_par_iter().map(move |c| {
                            let cell = XLSXSheetCell::new(Arc::clone(&current_sheet), r, c, None);
                            ((r, c), cell)
                        })
                    })
                    .collect();

                self._cells.extend(cells);
            }

            // Обновим максимальные значения
            self.max_row = self.max_row.max(row);
            self.max_column = self.max_column.max(col);

            Ok(cell)
        }
    }

    pub fn delete_cols(&mut self, idx: u16, amount: u16) -> Result<()> {
        // Remove cells in the specified columns
        self._cells.retain(|_, cell| {
            let cell = cell.lock().unwrap();
            cell.column < idx || cell.column >= idx + amount
        });

        // Update column numbers for remaining cells
        for (_, cell) in self._cells.iter() {
            let mut cell = cell.lock().unwrap();
            if cell.column > idx {
                cell.column -= amount;
                // Update the cell's letter coordinate
                let new_letter = crate::utils::column_number_to_letter(cell.column);
                cell.cell = format!("{}{}", new_letter, cell.row);
            }
        }

        // Update max_column if necessary
        self.max_column = self.max_column.saturating_sub(amount);

        Ok(())
    }

    pub fn delete_rows(&mut self, idx: u32, amount: u32) -> Result<()> {
        // Remove cells in the specified columns
        self._cells.retain(|_, cell| {
            let cell = cell.lock().unwrap();
            cell.row < idx || cell.row >= idx + amount
        });

        // Update column numbers for remaining cells
        for (_, cell) in self._cells.iter() {
            let mut cell = cell.lock().unwrap();
            if cell.row > idx {
                cell.row -= amount;
                // Update the cell's letter coordinate
                let new_letter = crate::utils::column_number_to_letter(cell.column);
                cell.cell = format!("{}{}", new_letter, cell.row);
            }
        }

        // Update max_column if necessary
        self.max_row = self.max_row.saturating_sub(amount);

        Ok(())
    }

    pub fn set_merged_cells(
        &mut self,
        start_row: u32,
        end_row: u32,
        start_column: u16,
        end_column: u16,
    ) -> Result<()> {
        // Iterate through all cells in the merge range
        for row in start_row..=end_row {
            for col in start_column..=end_column {
                if let Some(cell) = self._cells.get(&(row, col)) {
                    let mut cell = cell.lock().unwrap();
                    cell.is_merge = true;
                    cell.start_row = Some(start_row);
                    cell.end_row = Some(end_row);
                    cell.start_column = Some(start_column);
                    cell.end_column = Some(end_column);
                }
            }
        }

        Ok(())
    }
}
