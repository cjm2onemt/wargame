from gameunit import GameUnit


class OrcRider(GameUnit):
    def __init__(self,name=''):
        super().__init__(name=name)
        self.max_health=30
        self.health_meter=self.max_health
        self.unit_type='enemy'

    def info(self):
        print("I am a Orc,don't mess with me")