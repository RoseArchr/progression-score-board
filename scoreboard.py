import json
import os

class Scoreboard:
    def __init__(self):
        if self.is_file_empty():
            self.scores = {}
        else:
            self.scores = self.load_scores()

    def save_scores(self, scores: dict[str, int]):
        with open("data.json", "w") as file:
            json.dump(scores, file)

    def load_scores(self) -> dict[str, int]:
        with open("data.json") as file:
            return json.load(file)

    def is_file_empty(self) -> bool:
        return os.stat("data.json").st_size == 0

    def create_scoreboard(self, names: list[str]):
        for i in range(len(names)):
            self.scores[names[i]] = 0
        self.save_scores(self.scores)

    #def win(self, player: str):
        #self.scores[player] += 1
        #self.save(self.scores)