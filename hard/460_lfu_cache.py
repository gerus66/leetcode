# https://leetcode.com/problems/lfu-cache
# hard
# daily
from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.vault = dict()
        self.freq = defaultdict(OrderedDict)

    def _invalidate_lfu_key(self):
        lfu_key, _ = self.freq[min(self.freq.keys())].popitem(last=False)
        self.vault.pop(lfu_key)

    def _update_key(self, key, value=None):
        key_freq = self.vault[key][1]
        if len(self.freq[key_freq]) == 1:
            self.freq.pop(key_freq)
        else:
            self.freq[key_freq].pop(key)
        if value is not None:
            self.vault[key] = (value, key_freq+1)
        else:
            self.vault[key] = (self.vault[key][0], key_freq+1)
        self.freq[key_freq+1][key] = None

    def _add_key(self, key, value=None):
        self.vault[key] = (value, 1)
        self.freq[1][key] = None

    def get(self, key: int) -> int:
        if key not in self.vault:
            return -1
        self._update_key(key)
        return self.vault[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap:
            if key in self.vault:
                self._update_key(key, value)
            else:
                if len(self.vault) == self.cap:
                    self._invalidate_lfu_key()
                self._add_key(key, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
