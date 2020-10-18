import random
class HashTable:
    def __init__(self):
        self.dict = []
        for i in range(2):
            self.dict.append([])
        self.addresses = set()
    def _hash(self):
        while 1:
            i = random.randint(0,1)
            if i not in self.addresses:
                self.addresses.add(i)
                return i
    def _set(self, key, value):
        address = self._hash()
        self.dict[address].append([key, value])
        return self.dict
    def _get(self, key):
        for i in self.addresses:
            curPair = self.dict[i]
            for x in range(len(curPair)):
                if curPair[x][0] == key:
                    return curPair[x][1]
    def _keys(self):
        self.keys = []
        for i in self.addresses:
            curPair = self.dict[i]
            for x in range(len(curPair)):
                self.keys.append(curPair[x][0])
        return self.keys


hash_t = HashTable()
print(hash_t._set('grapes', 8))
print(hash_t._set('apples', 1000))
print(hash_t._set('oranges', 64))
print(hash_t._get('grapes'))
print(hash_t._get('apples'))
print(hash_t._get('oranges'))
print(hash_t._keys())
