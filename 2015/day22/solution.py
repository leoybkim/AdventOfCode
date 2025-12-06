import re
from copy import deepcopy
from heapq import heappop, heappush

from utils.input_reader import read_file


class Character:
    def __init__(self, hp):
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount


class Player(Character):
    def __init__(self, hp, mana):
        super().__init__(hp)
        self.mana = mana
        self.armour = 0

    def heal(self, amount):
        self.hp += amount


class Boss(Character):
    def __init__(self, hp, damage):
        super().__init__(hp)
        self.damage = damage


class SpellEffect:
    def __init__(self, name, duration, stat: dict):
        self.name = name
        self.duration = duration
        self.stat = stat

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Game:
    def __init__(self, player, boss, active_effects, mana_spent, hard_mode=False):
        self.player = deepcopy(player)
        self.boss = deepcopy(boss)
        self.active_effects = deepcopy(active_effects)
        self.mana_spent = mana_spent
        self.hard_mode = hard_mode
        self.spells = {
            "Magic Missile": {
                "cost": 53,
                "damage": 4
            },
            "Drain": {
                "cost": 73,
                "damage": 2,
                "heal": 2
            },
            "Shield": {
                "cost": 113,
                "armour": 7,
                "effect_duration": 6
            },
            "Poison": {
                "cost": 173,
                "damage": 3,
                "effect_duration": 6
            },
            "Recharge": {
                "cost": 229,
                "mana": 101,
                "effect_duration": 5
            }
        }

    def __eq__(self, other):
        return (self.player.hp == other.player.hp and
                self.player.mana == other.player.mana and
                self.boss.hp == other.boss.hp and
                len(self.active_effects) == len(other.active_effects) and
                all(effect in other.active_effects for effect in self.active_effects))

    def __hash__(self):
        return hash((self.player.hp, self.player.mana, self.boss.hp,
                     frozenset([(e.name, e.duration) for e in self.active_effects])))

    def __lt__(self, other):
        return self.mana_spent < other.mana_spent

    def apply_effects(self):
        self.player.armour = 0  # resets each turn
        next_active_effects = []
        for effect in self.active_effects:
            if effect.name == "Poison":
                self.boss.hp -= effect.stat["damage"]
            elif effect.name == "Recharge":
                self.player.mana += effect.stat["mana"]
            elif effect.name == "Shield":
                self.player.armour = effect.stat["armour"]

            effect.duration -= 1
            if effect.duration > 0:
                next_active_effects.append(effect)

        self.active_effects = next_active_effects

    def game_ended(self):
        return self.boss.hp <= 0 or self.player.hp <= 0

    def buy_spell(self, spell):
        self.player.mana -= self.spells[spell]["cost"]
        self.mana_spent += self.spells[spell]["cost"]

    def cast_spell(self, spell):
        if "effect_duration" in self.spells[spell]:
            effect_state = {k: v for k, v in self.spells[spell].items() if k not in ["cost", "effect_duration"]}
            new_effect = SpellEffect(name=spell,
                                     duration=self.spells[spell]["effect_duration"],
                                     stat=effect_state)
            self.active_effects = frozenset(list(self.active_effects) + [new_effect])
        else:
            if "damage" in self.spells[spell]:
                self.boss.take_damage(self.spells[spell]["damage"])
            if "heal" in self.spells[spell]:
                self.player.heal(self.spells[spell]["heal"])

    def play(self):
        """
        Simulate the current state: player takes turn and then boss takes turn.
        Then return generated next possible states.
        """
        next_states = []
        current_state = deepcopy(self)

        # explore all possible spell that can be cast in the next state
        for spell in self.spells:
            next_state = deepcopy(current_state)
            if next_state.player.mana < self.spells[spell]["cost"]:
                continue  # not enough mana

            if "effect_duration" in self.spells[spell]:
                if any(effect.name == spell for effect in next_state.active_effects):
                    continue  # equivalent spell is already in effect

            ###################
            ### Player Turn ###
            ###################

            # 0. hard mode
            if self.hard_mode:
                next_state.player.take_damage(1)
                if next_state.game_ended():
                    continue  # player lost

            # 1. buy spell
            next_state.buy_spell(spell)

            # 2. cast spell
            next_state.cast_spell(spell)

            # 3. apply current spells in effect
            next_state.apply_effects()

            # 4. check if player won
            if next_state.game_ended():
                next_states.append(next_state)  # player won
                continue

            #################
            ### Boss Turn ###
            #################

            # 1. boss Attacks
            next_state.player.take_damage(max(1, next_state.boss.damage - next_state.player.armour))

            # 2. check if boss won
            if next_state.game_ended():
                continue  # player lost

            # 3. apply current spells in effect
            next_state.apply_effects()

            # 4. check if player won
            if next_state.game_ended():
                next_states.append(next_state)  # player won
                continue

            next_states.append(next_state)

        return next_states


def parse_boss_stats(raw_input: str) -> tuple[int, int] | None:
    pattern = re.compile(
        r"^Hit Points: (\d+)\n"
        r"^Damage: (\d+)$",
        re.MULTILINE
    )

    match = pattern.search(raw_input)
    if match:
        hit_points = int(match.group(1))
        damage = int(match.group(2))
        return hit_points, damage
    else:
        return None


def find_min_mana_required(raw_input: str, hp=50, mana=500, hard=False) -> int:
    min_mana = float("inf")
    boss_hit_points, boss_damage = parse_boss_stats(raw_input)

    initial_player = Player(hp=hp, mana=mana)
    initial_boss = Boss(hp=boss_hit_points, damage=boss_damage)
    initial_state = Game(player=initial_player,
                         boss=initial_boss,
                         active_effects=frozenset(),
                         mana_spent=0,
                         hard_mode=hard)

    # priority queue that stores total mana spent and the game state
    pq = [initial_state]

    # visited states where key is the game state and the value is the cost to reach that state
    visited_states = {}

    while pq:
        current_state = heappop(pq)
        # only consider cheaper states
        if current_state.mana_spent < min_mana:
            # don't consider already visited state if it costs equal or more mana
            if current_state not in visited_states or current_state.mana_spent < visited_states[current_state]:
                visited_states[current_state] = current_state.mana_spent

                if current_state.boss.hp <= 0:
                    min_mana = min(min_mana, current_state.mana_spent)
                    continue

                # simulate current state and generate possible next states
                next_states = current_state.play()

                for state in next_states:
                    if state.player.hp > 0:
                        heappush(pq, state)

    return min_mana


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"What is the minimum mana required to win?: {find_min_mana_required(file)}")
    print(f"What is the minimum mana required to win in hard mode?: {find_min_mana_required(file, hard=True)}")
