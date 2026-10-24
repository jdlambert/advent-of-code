use std::collections::HashSet;

fn priority(item: char) -> u32 {
    match item {
        'a'..='z' => item as u32 - 'a' as u32 + 1,
        'A'..='Z' => item as u32 - 'A' as u32 + 27,
        _ => unreachable!(),
    }
}

fn part1(data: &[&str]) -> u32 {
    data.iter()
        .map(|line| {
            let left: HashSet<_> = line.get(..line.len() / 2).unwrap().chars().collect();
            let right: HashSet<_> = line.get(line.len() / 2..).unwrap().chars().collect();
            priority(*left.intersection(&right).next().unwrap())
        })
        .sum()
}

fn part2(data: &[&str]) -> u32 {
    data.chunks(3)
        .map(|lines| {
            let common = lines
                .iter()
                .map(|line| line.chars().collect())
                .reduce(|acc: HashSet<_>, bag| acc.intersection(&bag).cloned().collect())
                .unwrap();
            priority(*common.iter().next().unwrap())
        })
        .sum()
}

fn main() {
    let data: Vec<_> = include_str!("../input.txt").lines().collect();
    println!("Part 1: {}", part1(&data));
    println!("Part 2: {}", part2(&data));
}
