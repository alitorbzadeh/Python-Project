import random
from collections import OrderedDict

class Human():
    def __init__(self,name):
        self.name=name

    
class Players(Human):
    A_number=11
    B_number=11
    
    def random_selection(self):
        select=random.randint(a=0,b=2)
        if select==1:
            if Players.A_number!=0:
                Players.A_number-=1
                return "A"
            else:
                Players.B_number-=1
                return "B"
        else:
            if Players.B_number!=0:
                Players.B_number-=1
                return "B"
            else:
                Players.A_number-=1
                return "A"


Team_A=OrderedDict()
Team_B=OrderedDict()
for i in range(22):
    player=Players(name=input())
    res=player.random_selection
    if res=="A":
        Team_A[player.name]="A"
    else:
        Team_A[player.name]="B"

All_Players=Team_A|Team_B