My solutions for [Advent of Code](https://adventofcode.com/), one directory per year.

## Running

Put your adventofcode.com `cookie` header value in `./cookie`, then:

```sh
./advent.sh 2024 5          # create 2024/day05 from templates/python, or run it if it exists
./advent.sh 2024 5 x        # run against example.txt (Python solutions)
```

Inputs aren't committed; `advent.sh` fetches any missing `input.txt` before running.
