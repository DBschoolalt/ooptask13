import random
from characters.logger import Logger
from characters.characters import Knight, Mystic, Creature

def dictAll(oldtable):
    newtable = []
    for i in oldtable:
        newtable.append(i.toDict())
    return newtable

def charAll(oldtable):
    newtable = []
    for i in oldtable:
        if i["class"] == 'knight': 
            a = Knight(i["name"])
        elif i["class"] == 'mystic': 
            a = Mystic(i["name"])
        elif i["class"] == 'creature': 
            a = Creature(i["name"])
        a.setHP(i["hp"])
        print(a.name, a.hp, i["hp"])

        newtable.append(a)
    return newtable

class Game:
    def __init__(self):
        self.__alive = []
        self.__turn = 0
        self.__done = False
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

        if len(self.__alive) <= 1:
            Logger.print(f'------ {self.__alive[0].name} wins! ------')
            self.__done = True
    def list(self):
        for i in self.__alive:
            Logger.print(i.list())
        #time.sleep(1)
    def getState(self):
        return {'turn': self.__turn, 'alive': dictAll(self.__alive)}

    def setState(self, state):
        self.__alive = charAll(state['alive'])
        self.__turn = state['turn']
        Logger.print(f'------ State Set! ------')

    def play(self):
        while len(self.__alive) > 1:
            self.turn()

    def isDone(self):
        return self.__done
        