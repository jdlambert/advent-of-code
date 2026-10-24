type Pair = ((u32, u32), (u32, u32));

fn part1(pairs: &[Pair]) -> usize {
    pairs
        .iter()
        .filter(|((ll, lr), (rl, rr))| (ll <= rl && lr >= rr) || (rl <= ll && rr >= lr))
        .count()
}

fn part2(pairs: &[Pair]) -> usize {
    pairs
        .iter()
        .filter(|((ll, lr), (rl, rr))| ll <= rr && rl <= lr)
        .count()
}

fn range(input: &str) -> (u32, u32) {
    let (l, r) = input.split_once('-').unwrap();
    (l.parse::<u32>().unwrap(), r.parse::<u32>().unwrap())
}

fn main() {
    let data: Vec<_> = include_str!("../input.txt")
        .lines()
        .map(|line| {
            let (l, r) = line.split_once(',').unwrap();
            (range(l), range(r))
        })
        .collect();
    println!("Part 1: {}", part1(&data));
    println!("Part 2: {}", part2(&data));
}
