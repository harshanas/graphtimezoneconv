from time import gmtime, strftime

class timezone:
    def __init__(self):
        self.fb_timezones = {'1':[1, 00], '2': [2, 00], '3': [3, 00], '4': [4, 00], '5': [5, 00], '5.5': [5, 30], '6': [6, 00], '7': [7, 00],
             '8': [8, 00], '9': [9, 00], '9.5': [9, 30], '10': [10, 00], '11': [11, 00], '12': [12, 00],
             '-11': [-11, 00], '-10': [-10, 00], '-9': [-9, 00], '-8': [-8, 00], '-7': [-7, 00], '-6': [-6, 00], '-5': [-5, 00],
             '-4': [-4, 00],'-3.5': [-3, 30], '-3': [-3, 00], '-2': [-2, 00], '-1': [-1, 00]}

    def getcurrenttime(self, offset):
        newmin = newhour = 0
        currentgmthour = int(strftime("%H", gmtime()))
        currentgmtmin = int(strftime("%M", gmtime()))

        if currentgmtmin < 30:
            currentgmtmin += 60
            currentgmthour -= 1
        newmin = currentgmtmin + int(self.fb_timezones[offset][1])

        if newmin >= 60:
            newhour += (newmin // 60)
            newmin -= (newmin // 60)*60

        newhour += currentgmthour + int(self.fb_timezones[offset][0])

        if newhour >= 24:
            newhour -= (newhour // 24)*24

        return [newhour, newmin]

