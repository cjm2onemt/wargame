import abc
from comfunc import print_bold,possible_target
import random


class GameUnit(metaclass=abc.ABCMeta):
    def __init__(self, name=''):
        self.name = name
        self.enemy = None
        self.max_health=0
        self.health_meter = 0
        self.unit_type=None

    @abc.abstractmethod
    def info(self):
        pass

    def attack(self,Orc):
        injury = random.randint(10, 15)
        hurt_target = possible_target(self, Orc)
        hurt_target.health_meter = max(hurt_target.health_meter - injury, 0)
        print_bold('%s get damage:%d\t' % (hurt_target.name, injury))
        self.show_health(end='\t')
        Orc.show_health(end='\t')

    def heal(self,heal_blood=2,full_blood=True):
        if self.health_meter==self.max_health:
            return
        if full_blood:
            self.health_meter=self.max_health
        else:
            self.health_meter=max(self.health_meter+heal_blood,self.max_health)
        print_bold('you are HEALED')
        self.show_health(bold=True)
    def reset_health_meter(self):
        self.health_meter=self.max_health

    def show_health(self,bold=False,end='\n'):
        msg = '%s:%d' % (self.name, self.health_meter)
        if bold:
            print_bold(msg,end=end)
        else:
            print(msg,end=end)