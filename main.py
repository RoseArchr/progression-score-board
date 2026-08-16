import json
import os
from typing import Any

#player1 = "Rose"
#player2 = "Lily"

def win(player: str, player_scores: dict[str, int]):
    player_scores[player] += 1

def save(player_scores: dict[str, int]):
    with open("data.json", "w") as file:
        json.dump(player_scores, file)

def load() -> dict[str, int]:
    with open("data.json") as file:
        return json.load(file)

def is_file_empty() -> bool:
    return os.stat("data.json").st_size == 0

def new_game():
    player_scores = {}
    print("How many players?")
    players = int(input())
    for i in range(players):
        print(f"Enter player {i+1}:")
        player_scores[str(input())] = 0
    save(player_scores)

def main():
    if is_file_empty():
        print("no game data found, Creating new game.")
        new_game()
        print(load())
    else:
        print("game data found")
        player_scores = load()
        print(player_scores)

main()