import random
import datetime

DICE = [
        ["E6","D5","E4","E5","F5","F4"],
        ["A4","B5","C5","C6","D6","F6"],
        ["A1","C1","D1","D2","E2","F3"],        
        ["A3","B1","B2","A2","B3","C2"],        
        ["D3","B4","C3","C4","D4","E3"],
        ["A5","F2","A5","F2","B6","E1"],
        ["A6","F1","A6","F1","A6","F1"],
    ]

DICE_NO_DUPS = [
        ["E6","D5","E4","E5","F5","F4"],
        ["A4","B5","C5","C6","D6","F6"],
        ["A1","C1","D1","D2","E2","F3"],        
        ["A3","B1","B2","A2","B3","C2"],        
        ["D3","B4","C3","C4","D4","E3"],
        ["A5","F2","B6","E1"],
        ["A6","F1"],
    ]

class Dice:
    def __init__(self):
        self._dice = list(DICE)

    def roll(self):

        ret = []
        for d in self._dice:
            ret.append(random.choice(d))
        return ret
              
base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(number, base):
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    ret = result[::-1] or "0"
    return ret

def count_combinations():
    # Not really needed since you can multiply the lenghts
    # of the DICE_NO_DUPS. But just as a check. Took almost
    # 3 minutes to get 62208
    print(datetime.datetime.now())
    possibles = []    
    for i in range(int('5555555',6)+1):
        comb = to_base(i,6).rjust(7,'0')
        if comb.endswith('00000'):
            print(comb, len(possibles))
        roll = []
        for j in range(7):
            roll.append(DICE[j][int(comb[j])])    
        roll = sorted(roll)
        if roll not in possibles:
            possibles.append(roll)                            
    print('>>>',len(possibles))
    print(datetime.datetime.now())

if __name__ == '__main__':    
    count_combinations()