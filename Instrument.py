import numpy as np

class Prober:        
    def __init__(self, count) -> None:
        self.data = []
        self.count = [0]

        self.data.append([])
        for _ in range(1, count):
            self.data.append([])
            self.count.append(0)
        
    def __call__(self, v, offset=0):
        self.count[offset] = self.count[offset] + 1
        if(self.count[offset] % 4 == 0):
            self.data[offset].append(v)
    
    def get(self):
        if len(self.data[0]) == 0:
            return np.array([])

        out = np.array(self.data[0]).squeeze()
        for i in range(1, len(self.data)):
            a = np.array(self.data[i]).squeeze()
            out = np.concatenate((out, a), axis=1)
        return out

    
probe = Prober(3)
