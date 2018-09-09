import random


def print_bold(msg,end='\n'):
    print('\033[1m'+msg+'\033[0m',end=end)

def dotted_line(num=50):
    print('*'*num)

def possible_target(obj1,obj2):
    hurts = [id(obj1)] * 3 + [id(obj2)] * 7
    hurt_target = random.choice(hurts)
    if hurt_target==id(obj1):
        return obj1
    else:
        return obj2