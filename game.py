import random
# from characters.characters import Knight, Mystic, Creature
class logger:
    def __init__(self):
        self.log = ''
    def resetlog(self):
        self.log = ''
    def addtolog(self, text):
        self.log += text+'\n'
    def getlog(self):
        return self.log
    def print(self, text):
        print(text)
        self.addtolog(text)

Logger = logger()






class Character:
    class_name = 'character'

    def __init__(self, name, hp, dmg, heal_hp):
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__dmg = dmg
        self.__heal_hp = heal_hp
        #Logger.print(f"{self.__name} the {self.class_name} joins the game! (hp:{self.max_hp}, dmg:{self.__dmg}, heal:{self.__heal_hp})")

    def list(self):
        return f"{self.__name} the {self.class_name} (hp:{self.__hp}/{self.__max_hp}, dmg:{self.__dmg}, heal:{self.__heal_hp})"

    def hit(self, opponent):
        Logger.print(f"{self.__name} hits {opponent.name};   {opponent.name} receives {self.__dmg} damage ({opponent.hp-self.__dmg}/{opponent.max_hp})")
        opponent.getHit(self.__dmg)

    def getHit(self, dmg=0):
        self.__hp -= dmg
        
        if self.__hp <= 0:
            self.die()

    def die(self):
        Logger.print(f"{self.__name} had fallen")

    def heal(self):
        self.__hp += self.__heal_hp
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp
        Logger.print(f"{self.__name} heals by {self.__heal_hp} ({self.__hp}/{self.__max_hp})")

    def setHP(self, hp):
        self.__hp = hp

    def toDict(self):
        return {'name': self.__name, 'class': self.class_name, 'hp': self.__hp}

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

     


class Knight(Character):
    class_name = 'knight'
    def __init__(self, name):
        super().__init__(name, 30, 10, 5)

class Creature(Character):
    class_name = 'creature'
    def __init__(self, name):
        super().__init__(name, 60, 5, 1)

class Mystic(Character):
    class_name = 'mystic'
    def __init__(self, name):
        super().__init__(name, 20, 5, 10)
















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

        newtable.append(a)
    return newtable

def generateCharacterFromData(oldtable):
    newtable = []
    for i in oldtable:
        if i["class"] == 'Knight': 
            a = Knight(i["name"])
        elif i["class"] == 'Mystic': 
            a = Mystic(i["name"])
        elif i["class"] == 'Creature': 
            a = Creature(i["name"])

        newtable.append(a)
    return newtable

class Game:
    def __init__(self):
        self.__alive = []
        self.__turn = 0
        self.__done = False
    def new(self, characters):
        self.__alive = generateCharacterFromData(characters)
    def turn(self):
        Logger.resetlog()
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

        return Logger.getlog()
    def list(self):
        Logger.resetlog()
        for i in self.__alive:
            Logger.print(i.list())
        return Logger.getlog()
        #time.sleep(1)
    def getState(self):
        return {'turn': self.__turn, 'alive': dictAll(self.__alive)}

    def setState(self, state):
        self.__alive = charAll(state['alive'])
        self.__turn = state['turn']
        

    def play(self):
        while len(self.__alive) > 1:
            self.turn()

    def isDone(self):
        return self.__done
        