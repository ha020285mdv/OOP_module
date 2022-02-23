
class GameOver(Exception):
    def __init__(self, data):
        self.data = data


class EnemyDown(Exception):
    pass
