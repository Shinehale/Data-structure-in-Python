class HashTable:
    def __init__(self):
        self.size = 11
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
                nextSlot = self.reHash(hashValue, len(self.slots))
                while self.slots[nextSlot] is not None and \
                        self.slots[nextSlot] != key:
                    nextSlot = self.reHash(nextSlot, len(self.slots))
                if self.slots[nextSlot] is None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data

    def hashfunction(self, key, size):
        return key % size

    def reHash(self, oldHashValue, size):
        return (oldHashValue + 1) % size

    def get(self, key):
        startSlot = self.hashfunction(key, len(self.slots))

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
                position = self.reHash(position, len(self.slots))
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


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[22] = "chicken"
print(len(H))
