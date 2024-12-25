use pyo3::prelude::*;

#[pyfunction]
pub fn filter_special_tokens(seq: Vec<i32>, special_tokens: Vec<i32>) -> Vec<i32> {
    let mut seq = seq;
    let special_tokens: std::collections::HashSet<_> = special_tokens.into_iter().collect();

    while let Some(first) = seq.first() {
        if special_tokens.contains(first) {
            seq.remove(0);
        } else {
            break;
        }
    }

    while let Some(last) = seq.last() {
        if special_tokens.contains(last) {
            seq.pop();
        } else {
            break;
        }
    }

    seq
}
