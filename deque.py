class Deque:
    def __init__(self,maxlen):
        self._data = [None] * 10
        self._size = 0
        self._front = 0

    def __str__(self):
        return '%s,%s'%(self._front,self._data)

    def appendleft(self,d):
        if self._size == len(self._data):
            self.resize()
        self._size += 1
        self._front = (self._front-1)%len(self._data)
        self._data[self._front] = d

    def appendright(self,d):
        if self._size == len(self._data):
            self.resize()
        self._size += 1
        self._data[(self._front+self._size-1)%len(self._data)] = d

    def popleft(self):
        if self._size < len(self._data)/4:
            self.resize(False)
        self._size -= 1
        rval = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        return rval

    def popright(self):
        if self._size < len(self._data)/4:
            self.resize(False)
        self._size -= 1
        rval = self._data[self._front+self._size]
        self._data[self._front+self._size] = None
        return rval

    def resize(self,grow=True):
        if grow:
            old_data = self._data
            self._data = [None] * 2*len(old_data)
            for i in range(len(old_data)):
                self._data[i] = old_data[(self._front+i)%len(old_data)]
        else:
            old_data = self._data
            self._data = [None] * (len(old_data)/2)
            for i in range(self._size):
                print old_data[(self._front+i)%len(old_data)]
                self._data[i] = old_data[(self._front+i)%len(old_data)]
        self._front =0
dd = Deque(20)
print dd
dd.appendleft(2)
print dd
dd.appendright(3)
print dd
dd.popleft()
print dd
dd.popright()
print dd
