import sys
import os
import math

class PN_Pickup():
    def __init__(self):
        self.Data = './prime_number_list.txt'
        with open(self.Data) as fh:
            self.PN = [s.strip() for s in fh.readlines()]
            if self.PN[-1] == "":
                self.PN.pop()

    def write_result(self,x):
        x = [s + "\n" for s in x]
        with open(self.Data, mode='w') as fh:
            fh.writelines(x)

    def add_PN(self, x):
        self.PN.append(str(x))

    def find_PN(self, x):
        x_max = int(math.sqrt(x)) +1

        if(len(self.PN) == 0):
            s = 2
        else:
            s = int(self.PN[-1])
            s += 1
            for i in self.PN:
                if int(i) >= x_max:
                    break
                if x % int(i) == 0:
                    return -1

        for i in range(s, x_max, 1):
            if x % int(i) == 0:
                return -2

        if x > int(self.PN[-1]):
            self.add_PN(x)
            return 2

        return 1

    def prtParam(self):
        print(self.PN)
        #print(self.X)

if __name__ == "__main__":
    x = int(sys.argv[1])
    x = int(x)
    #x = 100
    p = PN_Pickup()
    for i in range(2, x, 1):
        r = p.find_PN(i)
        if r == 1:
            print(str(i) + ' --> Prime Number')
        elif r == 2:
            print(str(i) + ' --> New Prime Number')
        else:
            pass
            #print(str(i) + ' -->' + str(r))

    p.write_result(p.PN)
