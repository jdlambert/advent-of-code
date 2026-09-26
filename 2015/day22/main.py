import sys
import re
from dataclasses import dataclass, replace
import heapq

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

boss_hp, boss_damage = [int(num) for num in re.findall(r"\d+", data)]

@dataclass(order=True)
class State:
    mana_spent: int
    health_remaining: int
    mana_remaining: int
    boss_health_remaining: int
    shield_turns: int
    poison_turns: int
    recharge_turns: int
    player_turn: bool
    hard_mode: bool

def all_possible_turns(state):
    if state.player_turn and state.hard_mode:
        state = replace(state, health_remaining=state.health_remaining - 1)
        if state.health_remaining < 1:
            yield state
            return
    state = replace(
        state,
        boss_health_remaining=state.boss_health_remaining - (3 if state.poison_turns else 0),
        poison_turns=max(0, state.poison_turns - 1),
        mana_remaining=state.mana_remaining + (101 if state.recharge_turns else 0),
        recharge_turns=max(0, state.recharge_turns - 1),
        shield_turns=max(0, state.shield_turns - 1),
    )
    if not state.player_turn and state.boss_health_remaining > 0:
        incoming_damage = max(1, boss_damage - (7 if state.shield_turns else 0))
        yield replace(
            state,
            health_remaining = state.health_remaining - incoming_damage,
            player_turn=True
        )
    else:
        state = replace(state, player_turn=False)
        if state.boss_health_remaining < 1 or state.health_remaining < 1:
            yield state
            return
        if mana_state := try_spend_mana(state, 53):
            yield replace(
                mana_state,
                boss_health_remaining=state.boss_health_remaining - 4,
            )
        if mana_state := try_spend_mana(state, 73):
            yield replace(
                mana_state,
                boss_health_remaining=state.boss_health_remaining - 2,
                health_remaining=state.health_remaining + 2,
            )
        if not state.shield_turns and (mana_state := try_spend_mana(state, 113)):
            yield replace(
                mana_state,
                shield_turns=6
            )
        if not state.poison_turns and (mana_state := try_spend_mana(state, 173)):
            yield replace(
                mana_state,
                poison_turns=6
            )
        if not state.recharge_turns and (mana_state := try_spend_mana(state, 229)):
            yield replace(
                mana_state,
                recharge_turns=5
            )

def try_spend_mana(state: State, mana: int):
    if state.mana_remaining >= mana:
        return replace(
            state,
            mana_spent=state.mana_spent + mana,
            mana_remaining=state.mana_remaining - mana,
        )

def run_search(initial_state: State):
    frontier = [initial_state]
    while frontier:
        state = heapq.heappop(frontier)
        if state.boss_health_remaining < 1:
            return state.mana_spent
        if state.health_remaining < 1:
            continue
        for child in all_possible_turns(state):
            heapq.heappush(frontier, child)

start = State(
    mana_spent = 0,
    mana_remaining = 500,
    health_remaining = 50,
    boss_health_remaining = boss_hp,
    poison_turns = 0,
    shield_turns = 0,
    recharge_turns = 0,
    player_turn = True,
    hard_mode = False,
)

p1 = run_search(start)
p2 = run_search(replace(start, hard_mode=True))

print(f"Part one: {run_search(start)}")
print(f"Part two: {run_search(replace(start, hard_mode=True))}")