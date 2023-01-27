# https://leetcode.com/problems/concatenated-words
# hard
# daily
from typing import List


class Solution:
    @staticmethod
    def close_words(i, arr, d, next_d):
        while i < len(arr) and arr[i][1] != '~':
            d[arr[i][1]][1] -= 1
            if not d[arr[i][1]][1]:
                d[arr[i][1]][0] = False
                next_d[arr[i][1]][0] = False
            i += 1
        return i

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = {w: [True, 1] for w in words}
        arr = [(w, w) for w in words]
        concatenated = []
        while arr:
            arr.extend((k, '~') for k in d.keys())  # add primary words
            arr.sort()
            next_arr = set()
            next_d = {k: [v[0], 0] for k, v in d.items()}
            j_max = 0
            i = self.close_words(0, arr, d, next_d)
            while i < len(arr):
                if arr[i][1] == '~':  # take primary word as prefix
                    prefix = arr[i][0]
                    j = i + 1
                    while j < len(arr) and arr[j][0].startswith(prefix):
                        if arr[j][1] != '~' and d[arr[j][1]][0]:
                            reduced_w = arr[j][0][len(prefix):]
                            if reduced_w in d.keys():
                                concatenated.append(arr[j][1])
                                d[arr[j][1]][0] = False
                                next_d[arr[j][1]][0] = False
                            elif (reduced_w, arr[j][1]) not in next_arr:
                                next_arr.add((reduced_w, arr[j][1]))
                                next_d[arr[j][1]][1] += 1
                        j += 1
                    j_max = max(j_max, j-1)
                    if j > j_max:
                        self.close_words(j, arr, d, next_d)
                i += 1
            arr, d = list(next_arr), next_d
        return concatenated
