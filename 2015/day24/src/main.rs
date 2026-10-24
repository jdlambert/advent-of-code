use itertools::Itertools;

fn qe(partition: &[u64]) -> u64 {
    partition.iter().product()
}

fn best_first_partition(weights: &[u64], num_partitions: u64) -> Vec<u64> {
    let target = weights.iter().sum::<u64>() / num_partitions;
    (1..weights.len())
        .find_map(|k| {
            weights
                .iter()
                .copied()
                .combinations(k)
                .filter(|combo| combo.iter().sum::<u64>() == target)
                .min_by_key(|combo| qe(combo))
        })
        .unwrap()
}

fn main() {
    let items: Vec<u64> = include_str!("../input.txt")
        .lines()
        .map(|x| x.parse().unwrap())
        .collect();
    println!("{}", qe(&best_first_partition(&items, 3)));
    println!("{}", qe(&best_first_partition(&items, 4)));
}
