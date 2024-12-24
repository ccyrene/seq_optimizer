use pyo3::prelude::*;
use std::cmp::{max, min};

#[pyfunction]
pub fn find_longest_common_sequence(sequences: Vec<Vec<i32>>) -> Vec<i32> {
    if sequences.is_empty() {
        return Vec::new();
    }

    let mut left_sequence = sequences[0].clone();
    let mut total_sequence: Vec<i32> = Vec::new();

    for right_sequence in sequences.iter().skip(1) {
        let mut max_indices = (0, 0, 0, 0);
        let mut max_matches = 0;
        let left_length = left_sequence.len();
        let right_length = right_sequence.len();

        for i in 1..=(left_length + right_length) {
            let left_start = max(0, left_length as isize - i as isize) as usize;
            let left_stop = min(left_length, left_length + right_length - i);
            let right_start = max(0, i as isize - left_length as isize) as usize;
            let right_stop = min(right_length, i);

            if left_stop > left_start && right_stop > right_start {
                let matches = left_sequence[left_start..left_stop]
                    .iter()
                    .zip(&right_sequence[right_start..right_stop])
                    .filter(|(a, b)| a == b)
                    .count();

                if matches > max_matches {
                    max_matches = matches;
                    max_indices = (left_start, left_stop, right_start, right_stop);
                }
            }
        }

        let (left_start, left_stop, right_start, right_stop) = max_indices;
        total_sequence.extend(&left_sequence[..(left_start + left_stop) / 2]);
        left_sequence = right_sequence[(right_start + right_stop) / 2..].to_vec();
    }

    total_sequence.extend(left_sequence);
    total_sequence
}
