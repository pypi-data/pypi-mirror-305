use anyhow::{bail, Result};
use rayon::prelude::*;
use std::sync::{Arc, Mutex};

use crate::types::{cell::XLSXSheetCell, sheet::XLSXSheet};

#[derive(Debug, Clone)]
pub struct HelperSheet {
    pub sheets: Vec<Arc<Mutex<XLSXSheet>>>,
}

impl HelperSheet {
    pub fn new(sheets: Vec<Arc<Mutex<XLSXSheet>>>) -> Self {
        Self { sheets }
    }

    /// Поиск листа по наименованию
    pub fn find_sheet_by_name(&self, name: &str) -> Result<Option<Arc<Mutex<XLSXSheet>>>> {
        let sheet = self
            .sheets
            .par_iter()
            .find_first(|s| s.lock().unwrap().name == name)
            .cloned();

        Ok(sheet)
    }

    /// Поиск листа по шаблону regex
    pub fn find_sheet_by_pattern(&self, pattern: &str) -> Result<Option<Arc<Mutex<XLSXSheet>>>> {
        let re = regex::Regex::new(pattern).unwrap();

        let cell = self
            .sheets
            .par_iter()
            .find_first(|s| re.is_match(&s.lock().unwrap().name))
            .cloned();

        Ok(cell)
    }

    /// Поиск листа по индексу
    pub fn find_sheet_by_index(&self, idx: i32) -> Result<Option<Arc<Mutex<XLSXSheet>>>> {
        let cell = self
            .sheets
            .par_iter()
            .find_first(|s| s.lock().unwrap().index == idx)
            .cloned();

        Ok(cell)
    }

    /// Получение списка листов, исключая передаваесый список.
    pub fn get_sheets_without_names(
        &self,
        name_list: Vec<String>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheet>>>> {
        let cells = self
            .sheets
            .par_iter()
            .filter(|c| !name_list.contains(&c.lock().unwrap().name))
            .cloned()
            .collect();

        Ok(cells)
    }

    /// Получение списка листов, передаваемого списка листов .
    pub fn get_sheets_with_names(
        &self,
        name_list: Vec<String>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheet>>>> {
        let cells = self
            .sheets
            .par_iter()
            .filter(|c| name_list.contains(&c.lock().unwrap().name))
            .cloned()
            .collect();

        Ok(cells)
    }
}

#[derive(Debug, Clone)]
pub struct HelperCell;

impl HelperCell {
    /// Поиск ячейки по шаблону
    pub fn find_cell_by_pattern_regex(
        pattern: &str,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Option<Arc<Mutex<XLSXSheetCell>>>> {
        let re = regex::Regex::new(&regex::escape(pattern))?;
        let cell = cells.par_iter().find_map_first(|cell| {
            let cell_guard = cell.lock().unwrap();
            if re.is_match(&cell_guard.value.get_value_str()) {
                Some(Arc::clone(cell))
            } else {
                None
            }
        });

        Ok(cell)
    }

    // Поиск ячеек по шаблону
    pub fn find_cells_by_pattern_regex(
        pattern: &str,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re = regex::Regex::new(&regex::escape(pattern))?;

        let cells = cells
            .par_iter()
            .filter_map(|cell| {
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

    /// Поиск ячеек колонок для строк которые соответствуют патерну
    pub fn find_cells_for_rows_pattern_regex(
        pattern: &str,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
        col_stop: Option<u16>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re = regex::Regex::new(&regex::escape(pattern))?;

        let cells = cells
            .par_iter()
            .filter_map(|cell| {
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

    /// Поиск ячеек строк для колонок которые соответствуют патерну
    pub fn find_cells_for_cols_pattern_regex(
        pattern: &str,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
        row_stop: Option<u32>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re = regex::Regex::new(&regex::escape(pattern))?;

        let cells = cells
            .par_iter()
            .filter_map(|cell| {
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

    /// Поиск ячеек с помощью ИЛИ ячейки по патернам
    pub fn find_cells_multi_pattern_regex(
        pattern_1: &str,
        pattern_2: &str,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re1 = regex::Regex::new(&regex::escape(pattern_1))?;
        let re2 = regex::Regex::new(&regex::escape(pattern_2))?;

        let cells = cells
            .par_iter()
            .filter_map(|cell| {
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

    /// Поиск ячейки по буквенной координате A1 (cell)
    pub fn find_cell_by_cell(
        cell: &str,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Option<Arc<Mutex<XLSXSheetCell>>>> {
        let found_cell = cells.par_iter().find_map_first(|c| {
            let cell_guard = c.lock().unwrap();
            if cell_guard.cell == cell {
                Some(Arc::clone(c))
            } else {
                None
            }
        });

        Ok(found_cell)
    }

    /// Поиск ячейки по координате
    pub fn find_cell_by_coords(
        row: u32,
        col: u16,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Option<Arc<Mutex<XLSXSheetCell>>>> {
        let found_cell = cells.par_iter().find_map_first(|cell| {
            let cell_guard = cell.lock().unwrap();
            if cell_guard.row == row && cell_guard.column == col {
                Some(Arc::clone(cell))
            } else {
                None
            }
        });

        Ok(found_cell)
    }

    /// Поиск ячеек между шаьлонами
    pub fn find_cells_between_patterns(
        pattern_start: &str,
        pattern_end: &str,
        cells: &[Arc<Mutex<XLSXSheetCell>>],
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let re_start = regex::Regex::new(&regex::escape(pattern_start))?;
        let re_end = regex::Regex::new(&regex::escape(pattern_end))?;

        let mut cells = cells.to_vec();
        cells.sort_by_key(|cell| {
            let cell = cell.lock().unwrap();
            (cell.row, cell.column)
        });

        let rows_idx = cells
            .par_iter()
            .filter_map(|cell| {
                let cell = cell.lock().unwrap();
                let val = cell.value.get_value_str();

                if re_start.is_match(&val) || re_end.is_match(&val) {
                    Some(cell.row)
                } else {
                    None
                }
            })
            .collect::<Vec<_>>();

        let cells = cells
            .par_iter()
            .filter_map(|cell| {
                let cell_guard = cell.lock().unwrap();
                if rows_idx.len() >= 2 {
                    if cell_guard.row >= rows_idx[0] && cell_guard.row <= rows_idx[1] {
                        Some(Arc::clone(cell))
                    } else {
                        None
                    }
                } else if rows_idx.len() == 1 {
                    if cell_guard.row >= rows_idx[0] {
                        Some(Arc::clone(cell))
                    } else {
                        None
                    }
                } else {
                    None
                }
            })
            .collect::<Vec<_>>();

        Ok(cells)
    }

    /// Получить список всех ячеек в заданном диапазоне.
    pub fn iter_cells(
        min_row: u32,
        max_row: u32,
        min_col: u16,
        max_col: u16,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        if min_row > max_row || min_col > max_col {
            bail!("The coordinates of the cells were incorrectly transmitted");
        }

        let cells = cells
            .par_iter()
            .filter_map(|cell| {
                let cell_guard = cell.lock().unwrap();
                if cell_guard.row >= min_row
                    && cell_guard.row <= max_row
                    && cell_guard.column >= min_col
                    && cell_guard.column <= max_col
                {
                    Some(Arc::clone(cell))
                } else {
                    None
                }
            })
            .collect();

        Ok(cells)
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне строк
    pub fn find_cells_by_range_rows(
        start_row: u32,
        end_row: u32,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let cells = cells
            .par_iter()
            .filter_map(|cell| {
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

    /// Возвращаем все ячейки, которые находятся в диапазоне колонок
    pub fn find_cells_by_range_cols(
        start_col: u16,
        end_col: u16,
        cells: &Vec<Arc<Mutex<XLSXSheetCell>>>,
    ) -> Result<Vec<Arc<Mutex<XLSXSheetCell>>>> {
        let cells = cells
            .par_iter()
            .filter_map(|cell| {
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
}
