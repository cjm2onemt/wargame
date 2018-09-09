from comfunc import print_bold,dotted_line
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from gameuniterror import GameUnitError,IdxTooBigError
import random


class AttackOfTheOrcs(object):
    def __init__(self):
        self.huts = []
        self.player = None

    def _occupy_huts(self,n=5):
        occupants=['friend','enemy',None]
        for i in range(n):
            computer_choose=random.choice(occupants)
            if computer_choose=='friend':
                name='friend'+str(i+1)
                self.huts.append(Hut(i+1,Knight(name)))
            elif computer_choose == 'enemy':
                name = 'enemy' + str(i + 1)
                self.huts.append(Hut(i + 1, OrcRider(name)))
            else:
                self.huts.append(Hut(i+1,computer_choose))

    def get_hut_occupants(self):
        return [x.get_occupant_type() for x in self.huts]

    def show_mission(self):
        print_bold('MISSION:',end='\n')
        print('\t1.you see some huts')
        print('\t2.you must fight with Orc to occupy all the huts')
    def _play_choose(self):
        print('\tCurrent occupants:%s'%self.get_hut_occupants())
        idx=0
        flag=True
        while flag:
            try:
                idx = int(input('choose the hut from 1-5:'))
                if idx <= 0:
                    raise IdxTooBigError('not in 1-5!',103)
                    # raise GameUnitError('not in 1-5!',101)
            except ValueError as e:
                print_bold('the idx type must be int,but %s. please try again'%e)
                continue
            except IdxTooBigError as e:
                print(e)
                print(e.error_message)
                continue
            try:
                if self.huts[idx-1].is_acquired:
                    print('The hut which you choose has been required,choose another one')
                else:
                    flag=False
            except IndexError as e:
                print_bold('index range out ,must be 1-5,but %s. please try again' % e)
                continue

        return idx

    def play(self):
        self.show_mission()
        dotted_line()
        self._occupy_huts()
        # continu_play=True
        self.player=Knight()
        occupant_nums = 0 #已占领数量
        while occupant_nums<5:
            idx=self._play_choose()
            self.player.acquire_hut(self.huts[idx-1])
            if self.player.health_meter<=0:
                print('You lost:(better luck next time')
                break
            if self.huts[idx-1].is_acquired:
                occupant_nums+=1
        if occupant_nums== 5:
            print_bold('\nCongratulation! you win')

if __name__=='__main__':
    game=AttackOfTheOrcs()
    game.play()