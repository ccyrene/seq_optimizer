pub mod filter_special_tokens;
pub mod longest_common;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pymodule]
fn _seq_optimizer(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(
        longest_common::find_longest_common_sequence,
        m
    )?)?;

    m.add_function(wrap_pyfunction!(
        filter_special_tokens::filter_special_tokens,
        m
    )?)?;

    Ok(())
}
