from characters.logger import Logger

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