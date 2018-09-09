from gameunit import GameUnit
from comfunc import print_bold


class Knight(GameUnit):
    def __init__(self,name='foo'):
        super().__init__(name=name)
        self.max_health=50
        self.health_meter=self.max_health
        self.unit_type='friend'

    def info(self):
        print('I am Knight')

    def acquire_hut(self,hut):
        print_bold("Entering hut %d..." % hut.number, end=' ')
        if (isinstance(hut.occupant,GameUnit) and
                hut.occupant.unit_type=='enemy'):
            play_option=True
            self.show_health(end=' ')
            hut.occupant.show_health(end=' ')
            while play_option:
                play_option = input('attack?YES(y)/NO(n):')
                if play_option == 'n':
                    self.run_away()
                    break
                self.attack(hut.occupant)
                if hut.occupant.health_meter<=0:
                    print('kill Orc')
                    hut.acquire(self)
                    break
                if self.health_meter<=0:
                    print('you dead')
                    break
        else:
            if hut.get_occupant_type=='empty':
                print_bold('Hut is empty')
            else:
                print_bold('Hut is Signed')
            hut.acquire(self)
            self.heal()

    def run_away(self):
        print('RUNAWAY')
        self.enemy=None