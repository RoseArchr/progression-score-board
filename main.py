import json
import os

def win(player: str, player_scores: dict[str, int]) -> dict[str, int]:
    player_scores[player] += 1
    save(player_scores)
    return player_scores

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

def play(scores: dict[str, int]):
    in_progress = True
    while in_progress:
        print("Enter winner (or done to end):")
        i = str(input())
        if i == "done":
            in_progress = False
        elif i == "clear":
            print("starting a new game")
            new_game()
            in_progress = False
            play(load())
        elif i in scores:
            scores = win(i, scores)
            print(load())
        else:
            print("Invalid input")


def main():
    player_scores = {}
    if is_file_empty():
        print("no game data found, Creating new game.")
        new_game()
        print(load())
    else:
        print("game data found")
        player_scores = load()
        print(player_scores)

    play(player_scores)

main()