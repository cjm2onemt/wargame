class GameUnitError(Exception):
    def __init__(self, message='',code=100):
        super().__init__(self,message)
        self.adding='-'*50+'\n'
        self.code_dict={
            100: 'this is 100',
            101: 'this is 101',
            102: 'this is 102',
        }
        self.error_message='GameError:'
class IdxTooBigError(GameUnitError):
    def __init__(self,message='',code=102):
        super().__init__(message)
        try:
            self.error_message=self.code_dict[code]
        except KeyError as e:
            self.error_message+=self.code_dict[102]
        self.error_message=self.adding+self.error_message+'\n'+self.adding