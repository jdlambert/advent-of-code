use std::collections::HashMap;

struct Dir {
    subdirs: HashMap<String, Dir>,
    files: HashMap<String, usize>,
}

impl Dir {
    fn new() -> Self {
        Dir {
            subdirs: HashMap::new(),
            files: HashMap::new(),
        }
    }

    fn dir_size(&self) -> usize {
        self.subdirs.values().map(Self::dir_size).sum::<usize>()
            + self.files.values().sum::<usize>()
    }

    fn dir_sizes(&self) -> Vec<usize> {
        let mut sizes = vec![self.dir_size()];
        sizes.extend(self.subdirs.values().flat_map(Self::dir_sizes));
        sizes
    }
}

fn main() {
    let mut root = Dir::new();

    let mut path = Vec::new();

    for line in include_str!("../input.txt").lines().skip(1) {
        let mut dir = &mut root;
        for dir_name in path.iter() {
            dir = dir.subdirs.get_mut(dir_name).unwrap();
        }

        if line == "$ cd .." {
            path.pop();
        } else if line.starts_with("$ cd ") {
            let dir_name: String = line.chars().skip(5).collect();
            path.push(dir_name.clone());
            dir.subdirs.insert(dir_name, Dir::new());
        } else if line.chars().next().unwrap().is_ascii_digit() {
            let (size, filename) = line.split_once(' ').unwrap();
            dir.files
                .insert(String::from(filename), size.parse::<usize>().unwrap());
        }
    }

    println!(
        "Part 1: {}",
        root.dir_sizes()
            .iter()
            .filter(|&&size| size <= 100000)
            .sum::<usize>()
    );
    let need = 30000000 - (70000000 - root.dir_size());
    println!(
        "Part 2: {}",
        root.dir_sizes()
            .iter()
            .filter(|&&size| size >= need)
            .min()
            .unwrap()
    );
}
