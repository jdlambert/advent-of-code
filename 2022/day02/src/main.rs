type Game = Vec<(i32, i32)>;

fn part1(data: &Game) -> i32 {
    data.iter()
        .map(|(theirs, mine)| {
            1 + mine
                + if theirs == mine {
                    3
                } else if (theirs + 1) % 3 == *mine {
                    6
                } else {
                    0
                }
        })
        .sum()
}

fn part2(data: &Game) -> i32 {
    data.iter()
        .map(|(theirs, rule)| {
            let mine = if *rule == 0 {
                (theirs - 1).rem_euclid(3)
            } else if *rule == 1 {
                *theirs
            } else {
                (theirs + 1).rem_euclid(3)
            };
            3 * rule + 1 + mine
        })
        .sum()
}

fn simplify(input: &str) -> i32 {
    match input {
        "A" | "X" => 0,
        "B" | "Y" => 1,
        "C" | "Z" => 2,
        _ => unreachable!(),
    }
}

fn main() {
    let data: Game = include_str!("../input.txt")
        .lines()
        .map(|line| line.split_once(' ').unwrap())
        .map(|(a, b)| (simplify(a), simplify(b)))
        .collect();
    println!("Part 1: {}", part1(&data));
    println!("Part 2: {}", part2(&data));
}
