from custom_exceptions import GameOver
from custom_exceptions import EnemyDown
from models import Player
from models import Enemy
from models import Scores
from models import read_commands


def play():
    player_name = input("Enter your name: ")
    while True:
        try:
            if read_commands(input("Enter 'start' to begin the epic battle: "), game_started=False):
                break
        except ValueError:
            print("Try again")
        else:
            break
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score += 5
            print('You have won ' + str(level) + ' level!')
            print('You have earned 5 points! TOTAL points: ' + str(player.score))
            level += 1
            enemy = Enemy(level)
            player.level = level



if __name__ == '__main__':
    try:
        play()
    except GameOver as e:
        data = e.data
        Scores.save_scores(data)
        print("Game over! Never give up!")
        print('Your results is: {} level, you earned {} points'.format(data['level'], data['score']))
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
