
import time
import characters

from game import Game
from logger import Logger


g = Game()
g.new(characters.Knight('Joel'), characters.Mystic('Jeremy'), characters.Creature('Jessie'), characters.Mystic('Jon'))
g.play()
