use std::sync::{Arc, Mutex};

use core_rs::helper::{HelperCell, HelperSheet};
use pyo3::{exceptions::PyRuntimeError, prelude::*, types::PyList};

use crate::types::{cell::WrapperXLSXSheetCell, sheet::WrapperXLSXSheet};

#[pyclass]
#[pyo3(module = "core_xlsx", name = "HelperSheet")]
#[derive(Debug, Clone)]
pub struct WrapperHelperSheet(pub(crate) Arc<Mutex<HelperSheet>>);

#[pymethods]
impl WrapperHelperSheet {
    #[new]
    pub fn new(sheets: &Bound<'_, PyList>) -> PyResult<Self> {
        Python::with_gil(|_py| {
            let sheets = sheets
                .iter()
                .map(|s| WrapperXLSXSheet::from(&s).0)
                .collect();

            Ok(Self(Arc::new(Mutex::new(HelperSheet::new(sheets)))))
        })
    }

    #[getter]
    pub fn sheets(&self) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            let sheets = self
                .0
                .lock()
                .unwrap()
                .sheets
                .iter()
                .map(|s| WrapperXLSXSheet(s.clone()))
                .collect::<Vec<WrapperXLSXSheet>>();

            Ok(sheets)
        })
    }

    pub fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        Python::with_gil(|_py| {
            let class_name = slf.get_type().qualname()?;

            Ok(format!(
                "{}: sheets: {}",
                class_name,
                slf.borrow().0.lock().unwrap().sheets.len()
            ))
        })
    }

    /// Поиск листа по наименованию
    pub fn find_sheet_by_name(&self, name: &str) -> PyResult<Option<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_sheet_by_name(name)
                .map(|s| s.map(WrapperXLSXSheet))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск листа по шаблону regex
    pub fn find_sheet_by_pattern(&self, pattern: &str) -> PyResult<Option<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_sheet_by_pattern(pattern)
                .map(|s| s.map(WrapperXLSXSheet))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск листа по индексу
    pub fn find_sheet_by_index(&self, idx: i32) -> PyResult<Option<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_sheet_by_index(idx)
                .map(|s| s.map(WrapperXLSXSheet))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Получение списка листов, исключая передаваесый список.
    pub fn get_sheets_without_names(
        &self,
        name_list: Vec<String>,
    ) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .get_sheets_without_names(name_list)
                .map(|sheets| sheets.into_iter().map(WrapperXLSXSheet).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Получение списка листов, передаваемого списка листов .
    pub fn get_sheets_with_names(&self, name_list: Vec<String>) -> PyResult<Vec<WrapperXLSXSheet>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .get_sheets_with_names(name_list)
                .map(|sheets| sheets.into_iter().map(WrapperXLSXSheet).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }
}

#[pyclass]
#[pyo3(module = "core_xlsx", name = "HelperCell")]
#[derive(Debug, Clone)]
pub struct WrapperHelperSheetCell;

#[pymethods]
impl WrapperHelperSheetCell {
    /// Поиск ячейки по шаблону
    #[staticmethod]
    pub fn find_cell_by_pattern_regex(
        pattern: String,
        cells: Vec<WrapperXLSXSheetCell>,
    ) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cell_by_pattern_regex(&pattern, &cells)
                .map(|c| c.map(WrapperXLSXSheetCell))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек по шаблону
    #[staticmethod]
    pub fn find_cells_by_pattern_regex(
        pattern: String,
        cells: Vec<WrapperXLSXSheetCell>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cells_by_pattern_regex(&pattern, &cells)
                .map(|c| c.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек колонок для строк которые соответствуют патерну
    #[staticmethod]
    #[pyo3(signature=(pattern, cells, /, col_stop=None))]
    pub fn find_cells_for_rows_pattern_regex(
        pattern: String,
        cells: Vec<WrapperXLSXSheetCell>,
        col_stop: Option<u16>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cells_for_rows_pattern_regex(&pattern, &cells, col_stop)
                .map(|c| c.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек строк для колонок которые соответствуют патерну
    #[staticmethod]
    #[pyo3(signature=(pattern, cells, /, row_stop=None))]
    pub fn find_cells_for_cols_pattern_regex(
        pattern: String,
        cells: Vec<WrapperXLSXSheetCell>,
        row_stop: Option<u32>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cells_for_cols_pattern_regex(&pattern, &cells, row_stop)
                .map(|c| c.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек с помощью ИЛИ ячейки по патернам
    #[staticmethod]
    pub fn find_cells_multi_pattern_regex(
        pattern_1: String,
        pattern_2: String,
        cells: Vec<WrapperXLSXSheetCell>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cells_multi_pattern_regex(&pattern_1, &pattern_2, &cells)
                .map(|c| c.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячейки по буквенной координате A1 (cell)
    #[staticmethod]
    pub fn find_cell_by_cell(
        cell: String,
        cells: Vec<WrapperXLSXSheetCell>,
    ) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cell_by_cell(&cell, &cells)
                .map(|c| c.map(WrapperXLSXSheetCell))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячейки по координате
    #[staticmethod]
    pub fn find_cell_by_coords(
        row: u32,
        col: u16,
        cells: Vec<WrapperXLSXSheetCell>,
    ) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cell_by_coords(row, col, &cells)
                .map(|c| c.map(WrapperXLSXSheetCell))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек между шаьлонами
    #[staticmethod]
    pub fn find_cells_between_patterns(
        pattern_after: String,
        pattern_before: String,
        cells: Vec<WrapperXLSXSheetCell>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let cells: Vec<_> = cells.into_iter().map(|item| item.0).collect();

            HelperCell::find_cells_between_patterns(&pattern_after, &pattern_before, &cells)
                .map(|c| c.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }
}
