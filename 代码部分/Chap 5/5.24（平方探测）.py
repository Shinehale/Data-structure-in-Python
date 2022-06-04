"""
载荷因子设定为0.75
这样可以自动调整self.size 大小
但是本程序上限是1000以内
如果想要更多的
自行在reset函数中添加你想要的大小内的质数
"""
lam = 0.75


class HashTable:
    def __init__(self):
        self.size = 37
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashfunction(key, len(self.slots))

        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                times=1
                nextSlot = self.reHash(hashValue, len(self.slots),times)
                while self.slots[nextSlot] is not None and \
                        self.slots[nextSlot] != key:
                    times+=1
                    nextSlot = self.reHash(nextSlot, len(self.slots),times)
                if self.slots[nextSlot] is None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data
        if len(self) >= self.size * 0.75:
            self.reset(self.size)

    def hashfunction(self, key, size):
        return key % size

    def reHash(self, oldHashValue, size,value):
        return (oldHashValue + value**2) % size

    def get(self, key):
        startSlot = self.hashfunction(key, len(self.slots))
        times=1
        data = None
        stop = False
        found = False
        position = startSlot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.reHash(position, len(self.slots),times)
                times+=1
                if position == startSlot:
                    stop = False
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        ans = 0
        for item in self.slots:
            if item is not None:
                ans += 1
        return ans

    def __contains__(self, item):
        ans = self.get(item)
        if ans is None:
            return False
        else:
            return True

    def __delitem__(self, key):
        startSlot = self.hashfunction(key, len(self.slots))
        times=1
        stop = False
        found = False
        position = startSlot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                self.data[position] = None
                self.slots[position] = None
            else:
                position = self.reHash(position, len(self.slots),times)
                times+=1
                if position == startSlot:
                    stop = False

    def reset(self, size):
        S = [11, 37, 79, 167, 349, 647, 991]
        re = []
        pos = S.index(size)
        for i in range(self.size):
            if self.slots[i] is not None:
                re.append((self.slots[i], self.data[i]))
        if pos == 6:
            print("The number is out of range!!")
            return
        self.size = S[pos + 1]
        self.slots = [None] * self.size
        self.data = [None] * self.size
        for item in re:
            self.put(item[0], item[1])

H=HashTable()
for i in range(15):
    if i ==0:
        continue
    H[i**3]=i**2
print(H.slots)
for i in range(15):
    print(H[i**3])
"""
平方探测功能已经完成
"""