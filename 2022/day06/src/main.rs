use std::collections::HashSet;

fn first_n_distinct(data: &str, n: usize) -> usize {
    data.chars()
        .collect::<Vec<_>>()
        .windows(n)
        .enumerate()
        .find_map(|(i, chars)| {
            if chars.iter().collect::<HashSet<_>>().len() == n {
                Some(i + n)
            } else {
                None
            }
        })
        .unwrap()
}

fn part1(data: &str) -> usize {
    first_n_distinct(data, 4)
}

fn part2(data: &str) -> usize {
    first_n_distinct(data, 14)
}

fn main() {
    let data = include_str!("../input.txt").trim();
    println!("Part 1: {}", part1(data));
    println!("Part 2: {}", part2(data));
}
