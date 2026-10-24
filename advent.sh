#!/usr/bin/env bash
# Usage: ./advent.sh YEAR DAY [args...]
#
# Creates YEAR/dayNN from templates/python if it doesn't exist, fetches
# input.txt if it's missing, then runs every solution in the directory:
#   main.py, Cargo.toml (src/main.rs), main.go, main.clj, main.c
# Extra args are passed through (e.g. `x` makes the Python solutions read example.txt).

ROOT=$(cd "$(dirname "$0")" && pwd)

if [[ $# -lt 2 || ! $1 =~ ^[0-9]{4}$ || ! $2 =~ ^[0-9]{1,2}$ ]]; then
  echo "Usage: ./advent.sh YEAR DAY [args...]"
  exit 1
fi

YEAR=$1
DAY=$((10#$2))
shift 2
DIR=$(printf "%s/%s/day%02d" "$ROOT" "$YEAR" "$DAY")

echo "$YEAR DAY $DAY"

if [ ! -d "$DIR" ]; then
  mkdir -p "$ROOT/$YEAR"
  cp -r "$ROOT/templates/python" "$DIR"
  CREATED=1
fi

if [ ! -f "$DIR/input.txt" ]; then
  if [ ! -f "$ROOT/cookie" ]; then
    echo "No cookie file! Put your adventofcode.com cookie header in $ROOT/cookie"
    exit 1
  fi
  curl -sf "https://adventofcode.com/$YEAR/day/$DAY/input" \
    -H "cookie: $(cat "$ROOT/cookie")" \
    -A "github.com/jdlambert advent.sh" \
    -o "$DIR/input.txt"
  if [ $? -ne 0 ]; then
    echo "Input not available!"
    rm -f "$DIR/input.txt"
    [ -n "$CREATED" ] && rm -rf "$DIR" && rmdir "$ROOT/$YEAR" 2> /dev/null
    exit 1
  fi
  echo "Input fetched!"
fi

if [ -n "$CREATED" ]; then
  echo "Directory created!"
  exit 0
fi

cd "$DIR" || exit 1
RAN=0
FAILED=0

run() {
  echo "--- $1"
  RAN=1
  shift
  "$@" || FAILED=1
}

run_c() {
  BIN=$(mktemp)
  cc -O2 -o "$BIN" main.c && "$BIN" "$@"
  STATUS=$?
  rm -f "$BIN"
  return $STATUS
}

[ -f main.py ] && run Python python3 main.py "$@"
[ -f Cargo.toml ] && run Rust cargo run --release --quiet -- "$@"
[ -f main.go ] && run Go go run . "$@"
[ -f main.clj ] && run Clojure clojure -M main.clj "$@"
[ -f main.c ] && run C run_c "$@"

if [ $RAN -eq 0 ]; then
  echo "No solution found in $DIR"
  exit 1
fi
exit $FAILED
