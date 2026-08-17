from scoreboard import *

def play(sb: Scoreboard):
    in_progress = True
    scores = sb.load_scores()
    while in_progress:
        print("Enter winner (or done to end):")
        i = str(input())
        if i == "done":
            in_progress = False
        elif i in scores:
            scores = win(i, scores)
            print(scores)
        else:
            print("Invalid input")
    sb.save_scores(scores)

def win(player: str, scores: dict[str, int]) -> dict[str, int]:
    scores[player] += 1
    return scores

def get_names() -> list[str]:
    print("How many players?")
    n = int(input())
    names = []
    for i in range(n):
        print(f"Enter player {i+1}: ")
        names.append(input())
    return names

def main():
    sb = Scoreboard()

    if sb.is_file_empty():
        print("no game data found, Creating new game.")
        sb.create_scoreboard(get_names())
        print(sb.scores)
    else:
        print("game data found")
        print(sb.scores)

    play(sb)

main()