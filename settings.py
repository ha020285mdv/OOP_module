from enum import Enum

NUMBER_OF_LIVES = 3

FILE_PATH = 'scores.txt'

REZULT = {12: 1, 23: 1, 31: 1, 11: 0, 22: 0, 33: 0, 13: -1, 21: -1, 32: -1}

# 1 wizard     1х2 = 1   1х1 = 0   1х3 = -1
# 2 warrior    2х3 = 1   2х2 = 0   2х1 = -1
# 3 robber     3х1 = 1   3х3 = 0   3х2 = -1

class Weapon(Enum):
    """Entity to store possible attacks|defences"""
    WIZARD = 1
    WARRIOR = 2
    ROBBER = 3

MENU = {
        'show scores': 'see top-10 results',
        'exit': 'quit',
        'help': 'see menu'
        }
