class Flash():
    def __init__(self):
        self._mx = 137438953472
        self._lev = 0
        
    def get(self, v):
        if (self._lev + v) <= self._mx:
            self._lev += v
        else:
            self._lev = self._mx
            
    def space(self):
        print("Осталось на диске: ", int((self._mx - self._lev)/1024/1024/1024), "GB")
        print("Заполнено: ", int(self._lev/1024/1024/1024), "GB")
        

ram = Flash()
ram.space()
ram.get(38514898059)
ram.space()
