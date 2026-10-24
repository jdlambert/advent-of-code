fn part1(mut piles: Vec<Vec<char>>, ops: Vec<(usize, usize, usize)>) -> String {
    for (count, from, to) in ops {
        for _ in 0..count {
            let mover = piles[from].pop().unwrap();
            piles[to].push(mover);
        }
    }
    piles.iter().filter_map(|pile| pile.last()).collect()
}

fn part2(mut piles: Vec<Vec<char>>, ops: Vec<(usize, usize, usize)>) -> String {
    for (count, from, to) in ops {
        let mut mover = Vec::new();
        for _ in 0..count {
            mover.push(piles[from].pop().unwrap());
        }
        piles[to].extend(mover.iter().rev());
    }
    piles.iter().filter_map(|pile| pile.last()).collect()
}

fn main() {
    let (piles_str, ops_str) = include_str!("../input.txt").split_once("\n\n").unwrap();
    let pile_count = piles_str.lines().rev().next().unwrap().len();
    let mut piles: Vec<Vec<_>> = vec![Vec::new(); pile_count];
    for line in piles_str.lines().rev().skip(1) {
        for (i, c) in line.chars().enumerate() {
            if c.is_alphabetic() {
                piles[(i - 1) / 4].push(c)
            }
        }
    }
    let ops: Vec<_> = ops_str
        .lines()
        .map(|line| {
            let splits: Vec<_> = line.split_whitespace().collect();
            (
                splits[1].parse::<usize>().unwrap(),
                splits[3].parse::<usize>().unwrap() - 1,
                splits[5].parse::<usize>().unwrap() - 1,
            )
        })
        .collect();

    println!("Part 1: {}", part1(piles.clone(), ops.clone()));
    println!("Part 2: {}", part2(piles.clone(), ops.clone()));
}
