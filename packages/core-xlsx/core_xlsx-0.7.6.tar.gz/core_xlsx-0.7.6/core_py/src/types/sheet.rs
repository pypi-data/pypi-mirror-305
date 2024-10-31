use core_rs::types::{sheet::XLSXSheet, DEFAULT_COL, DEFAULT_ROW};
use pyo3::{
    exceptions::PyRuntimeError,
    prelude::*,
    types::{PyDict, PyList},
};
use std::sync::{Arc, Mutex};

use super::cell::WrapperXLSXSheetCell;

macro_rules! extract_sheet {
    ($obj:expr, $($attr:ident),+) => {
        {
            let sheet = if $obj.is_instance_of::<PyDict>() {
                XLSXSheet {
                    $($attr: $obj.get_item(stringify!($attr)).unwrap().extract().unwrap(),)+
                    ..Default::default()
                }
            } else {
                XLSXSheet {
                    $($attr: $obj.getattr(stringify!($attr)).unwrap().extract().unwrap(),)+
                    ..Default::default()
                }
            };

            WrapperXLSXSheet(Arc::new(Mutex::new(sheet)))
        }
    };
}

#[pyclass]
#[pyo3(module = "core_xlsx", name = "XLSXSheet", subclass)]
#[derive(Debug, Clone)]
pub struct WrapperXLSXSheet(pub(crate) Arc<Mutex<XLSXSheet>>);

impl From<&Bound<'_, PyAny>> for WrapperXLSXSheet {
    fn from(obj: &Bound<'_, PyAny>) -> Self {
        let wrapper = extract_sheet!(obj, name, index, max_row, max_column);

        let cells_iter = if obj.is_instance_of::<PyDict>() {
            obj.get_item("cells").unwrap()
        } else {
            obj.getattr("cells").unwrap()
        }
        .downcast::<PyList>()
        .unwrap()
        .iter();

        let cells = cells_iter
            .map(|c| WrapperXLSXSheetCell::from(&c))
            .map(|w| {
                let cell = w.0.lock().unwrap();
                ((cell.row, cell.column), Arc::clone(&w.0))
            })
            .collect();

        if let Ok(mut sheet) = wrapper.0.lock() {
            sheet._cells = cells;
        }

        wrapper
    }
}

#[pymethods]
impl WrapperXLSXSheet {
    pub fn __repr__(slf: &Bound<'_, Self>) -> PyResult<String> {
        Python::with_gil(|_py| {
            let slf = slf.borrow();
            let slf_lock = slf.0.lock().unwrap();
            Ok(format!(
                "XLSXSheet ({}) cells: {}",
                slf_lock.name,
                slf_lock.cells().collect::<Vec<_>>().len()
            ))
        })
    }

    #[new]
    #[pyo3(signature=(name, index, rows=DEFAULT_ROW, cols=DEFAULT_COL))]
    pub fn new(name: String, index: i32, rows: u32, cols: u16) -> PyResult<Self> {
        Python::with_gil(|_py| {
            let sheet = XLSXSheet::new(name, index, rows, cols);

            Ok(Self(sheet))
        })
    }

    #[getter]
    pub fn name(&self) -> PyResult<String> {
        Python::with_gil(|_py| Ok(self.0.lock().unwrap().name.clone()))
    }

    #[getter]
    pub fn max_row(&self) -> PyResult<u32> {
        Python::with_gil(|_py| Ok(self.0.lock().unwrap().max_row))
    }

    #[getter]
    pub fn max_column(&self) -> PyResult<u16> {
        Python::with_gil(|_py| Ok(self.0.lock().unwrap().max_column))
    }

    #[getter]
    pub fn index(&self) -> PyResult<i32> {
        Python::with_gil(|_py| Ok(self.0.lock().unwrap().index))
    }

    #[getter]
    pub fn cells(&self) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            let sheet = self.0.lock().unwrap();
            let cells = sheet
                .cells()
                .map(|c| WrapperXLSXSheetCell(Arc::clone(c)))
                .collect();

            Ok(cells)
        })
    }

    pub fn write_cell(
        &mut self,
        row: u32,
        col: u16,
        value: String,
    ) -> PyResult<WrapperXLSXSheetCell> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .write_cell(row, col, &value)
                .map(|cell| WrapperXLSXSheetCell(Arc::clone(&cell)))
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to write cell: {}", e)))
        })
    }

    pub fn delete_cols(&mut self, idx: u16, cols: u16) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .delete_cols(idx, cols)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to delete cols: {}", e)))
        })
    }

    pub fn delete_rows(&mut self, idx: u32, rows: u32) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .delete_rows(idx, rows)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to delete rows: {}", e)))
        })
    }

    pub fn set_merged_cells(
        &mut self,
        start_row: u32,
        end_row: u32,
        start_column: u16,
        end_column: u16,
    ) -> PyResult<()> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .set_merged_cells(start_row, end_row, start_column, end_column)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed Merged cells{}", e)))
        })
    }

    #[pyo3(signature=(min_row=None, max_row=None, min_col=None, max_col=None))]
    pub fn iter_cells(
        &self,
        min_row: Option<u32>,
        max_row: Option<u32>,
        min_col: Option<u16>,
        max_col: Option<u16>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .iter_cells(min_row, max_row, min_col, max_col)
                .map(|cells| {
                    cells
                        .into_iter()
                        .map(|c| WrapperXLSXSheetCell(Arc::clone(c)))
                        .collect()
                })
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячейки по шаблону
    pub fn find_cell_by_pattern_regex(
        &self,
        pattern: &str,
    ) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cell_by_pattern_regex(pattern)
                .map(|cell| cell.map(|c| WrapperXLSXSheetCell(Arc::clone(&c))))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек по шаблону
    pub fn find_cells_by_pattern_regex(
        &self,
        pattern: &str,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_by_pattern_regex(pattern)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек колонок для строк которые соответствуют патерну
    #[pyo3(signature=(pattern, col_stop=None))]
    pub fn find_cells_for_rows_pattern_regex(
        &self,
        pattern: &str,
        col_stop: Option<u16>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_for_rows_pattern_regex(pattern, col_stop)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек строк для колонок которые соответствуют патерну
    #[pyo3(signature=(pattern, row_stop=None))]
    pub fn find_cells_for_cols_pattern_regex(
        &self,
        pattern: &str,
        row_stop: Option<u32>,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_for_cols_pattern_regex(pattern, row_stop)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек с помощью ИЛИ ячейки по патернам
    pub fn find_cells_multi_pattern_regex(
        &self,
        pattern_1: &str,
        pattern_2: &str,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_multi_pattern_regex(pattern_1, pattern_2)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячейки по буквенной координате A1 (cell)
    pub fn find_cell_by_cell(&self, cell: &str) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cell_by_cell(cell)
                .map(|cell| cell.map(WrapperXLSXSheetCell))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячейки по координате
    pub fn find_cell_by_coords(
        &self,
        row: u32,
        col: u16,
    ) -> PyResult<Option<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cell_by_coords(row, col)
                .map(|cell| cell.map(WrapperXLSXSheetCell))
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Поиск ячеек между шаьлонами
    pub fn find_cells_between_patterns(
        &self,
        pattern_after: &str,
        pattern_before: &str,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_between_patterns(pattern_after, pattern_before)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне строк
    pub fn find_cells_by_range_rows(
        &self,
        start_row: u32,
        end_row: u32,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_by_range_rows(start_row, end_row)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }

    /// Возвращаем все ячейки, которые находятся в диапазоне колонок
    pub fn find_cells_by_range_cols(
        &self,
        start_col: u16,
        end_col: u16,
    ) -> PyResult<Vec<WrapperXLSXSheetCell>> {
        Python::with_gil(|_py| {
            self.0
                .lock()
                .unwrap()
                .find_cells_by_range_cols(start_col, end_col)
                .map(|cells| cells.into_iter().map(WrapperXLSXSheetCell).collect())
                .map_err(|e| PyRuntimeError::new_err(format!("{}", e)))
        })
    }
}
