import random
import csv

from custom_exceptions import EnemyDown
from custom_exceptions import GameOver

from settings import NUMBER_OF_LIVES
from settings import REZULT
from settings import MENU
from settings import FILE_PATH
from settings import Weapon as W


class Enemy:
    """Class of Enemy entity"""
    def __init__(self, level: int):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.choice([1, 2, 3])

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """Class of Player entity"""
    def __init__(self, name, lives=NUMBER_OF_LIVES, score=0, allowed_attacks=None):
        self.name = name
        self.lives = lives
        self.score = score
        self.level = 1

    @staticmethod
    def fight(attack, defense):
        option_of_fighting = int(str(attack) + str(defense))
        return REZULT[option_of_fighting]

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver({'name': self.name, 'score': self.score, 'level': self.level})

    def attack(self, enemy_obj):
        while True:
            try:
                input_text = "Enter the number of attack: 1 wizard, 2 warrior or 3 robber: "
                user_attack = read_commands(input(input_text))
            except ValueError:
                print("Try again")
            else:
                break

        enemy_defence = Enemy.select_attack()
        fighting_result = Player.fight(user_attack, enemy_defence)

        if fighting_result == 0:
            print("It's a draw!")

        elif fighting_result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1

        else:
            print("You missed!")

    def defence(self, enemy_obj):
        enemy_attack = Enemy.select_attack()
        while True:
            try:
                input_text = "Enter the number of defence: 1 wizard, 2 warrior or 3 robber: "
                user_defence = read_commands(input(input_text))
            except ValueError:
                print("Try again")
            else:
                break

        fighting_result = Player.fight(enemy_attack, user_defence)

        if fighting_result == 0:
            print("It's a draw!")

        elif fighting_result == 1:
            print("You defended successfully!")

        else:
            print("You missed!")
            self.decrease_lives()


class Scores:
    """Class was created to manage of scoring"""
    @staticmethod
    def save_scores(data, path=FILE_PATH):
        saved_scores = Scores.get_scores()
        saved_scores.append((data['name'], int(data['score']), int(data['level'])))
        saved_scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
        top10_scores = saved_scores[:10]

        with open(path, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['name', 'score', 'level']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in top10_scores:
                line = {'name': row[0], 'score': row[1], 'level': row[2]}
                writer.writerow(line)

    @staticmethod
    def get_scores(path=FILE_PATH):
        all_scores = []
        with open(path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_scores.append((row['name'], int(row['score']), int(row['level'])))
        return all_scores

    @staticmethod
    def print_scores():
        print(6 * '*' + 'TOP-10 results:' + 6 * '*')
        for row in Scores.get_scores():
            print(f'{row[0]}: {row[1]} points on {row[2]} level')
        print(27 * '*' + '\n')



def read_commands(users_input, game_started=True):
    """Function to manage users input.
    Manage behavior of program depending entered data"""
    users_input.lower()

    if users_input == 'exit':
        raise KeyboardInterrupt

    if users_input == 'show scores':
        Scores.print_scores()

    if users_input == 'help':
        print('Commands:')
        for command, meanning in MENU.items():
            print(f" * Enter '{command}' to {meanning}")
        raise ValueError

    if users_input == 'start' and game_started is False:
        return True

    if game_started:
        if int(users_input) in [W.WARRIOR.value, W.WIZARD.value, W.ROBBER.value]:
            return int(users_input)
        else:
            raise ValueError
    else:
        raise ValueError

