import random
from characters.logger import Logger

class Game:
    def __init__(self):
        self.__alive = []
        self.__turn = 0
    def new(self, characters):
        self.__alive = list(characters)
    def turn(self):
        self.__turn += 1
        Logger.print(f" -- turn {self.__turn} --")
        for character in self.__alive:
            if character.hp <= 0:
                self.__alive.remove(character)

        for character in self.__alive:
            if character.hp <= 0:
                self.__alive.remove(character)
                break
            move = random.randint(1, 2)
            if move == 2 and character.hp >= character.max_hp:
                move = 1
            if move == 1:
                target = self.__alive.copy()
                target.remove(character)
                if len(target) <= 0:
                    continue
                character.hit(random.choice(target))
            elif move == 2:
                character.heal()
            if character.hp <= 0:
                self.__alive.remove(character)
        #time.sleep(1)

    def play(self):
        while len(self.__alive) > 1:
            self.turn()
        Logger.print(f'------ {self.__alive[0].name} wins! ------')