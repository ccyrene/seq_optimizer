use pyo3::prelude::*;
use std::cmp;

#[pyfunction]
pub fn find_longest_common_sequence(sequences: Vec<Vec<i32>>) -> Vec<i32> {
    let mut left_sequence = sequences[0].clone();
    let mut left_length = left_sequence.len();
    let mut total_sequence = Vec::new();

    for right_sequence in sequences.iter().skip(1) {
        let right_length = right_sequence.len();
        let mut max_ = 0.0;
        let mut max_indices = (left_length, left_length, 0, 0);

        for i in 1..=(left_length + right_length) {
            let eps = i as f64 / 10000.0;

            let left_start = cmp::max(0, left_length as isize - i as isize) as usize;
            let left_stop = cmp::min(left_length, left_length + right_length - i);
            let left = &left_sequence[left_start..left_stop];

            let right_start = cmp::max(0, i as isize - left_length as isize) as usize;
            let right_stop = cmp::min(right_length, i);
            let right = &right_sequence[right_start..right_stop];

            if left.len() != right.len() {
                panic!("Bug in 'longest_common' function: subsequence lengths do not match.");
            }

            let matches = left
                .iter()
                .zip(right.iter())
                .filter(|(&l, &r)| l == r)
                .count();

            let matching = matches as f64 / i as f64 + eps;
            if matches > 1 && matching > max_ {
                max_ = matching;
                max_indices = (left_start, left_stop, right_start, right_stop);
            }
        }

        let (left_start, left_stop, right_start, right_stop) = max_indices;
        let left_mid = (left_stop + left_start) / 2;
        let right_mid = (right_stop + right_start) / 2;

        total_sequence.extend_from_slice(&left_sequence[..left_mid]);
        left_sequence = right_sequence[right_mid..].to_vec();
        left_length = left_sequence.len();
    }

    total_sequence.extend_from_slice(&left_sequence);
    total_sequence
}
