from comfunc import print_bold


class Hut(object):
    def __init__(self, number, occupant):
        self.number = number
        self.occupant = occupant
        self.is_acquired = False

    def acquire(self, new_occupant):
        self.occupant=new_occupant
        self.is_acquired = True
        print_bold('Good Job. acquire Hut%d'%self.number,end=' ')

    def get_occupant_type(self):
        if self.is_acquired:
            occupant_type='acquired'
        elif self.occupant is None:
            occupant_type='empty'
        else:
            occupant_type=self.occupant.unit_type
        return occupant_type