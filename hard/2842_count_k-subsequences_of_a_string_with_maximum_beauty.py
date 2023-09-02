# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty
# hard
# missed - contest biweekly 112
from collections import Counter, defaultdict
from math import comb


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        f_dict = Counter(s)
        f_dict_rev = defaultdict(int)
        for kk, v in f_dict.items():
            f_dict_rev[v] += 1
        if k > sum(f_dict_rev.values()):
            return 0

        fs_needed, ans = k, 1
        for kk in sorted(f_dict_rev.keys(), reverse=True):
            if fs_needed <= f_dict_rev[kk]:
                ans *= comb(f_dict_rev[kk], fs_needed) * kk ** fs_needed
                break
            ans *= kk ** f_dict_rev[kk]
            fs_needed -= f_dict_rev[kk]
        return ans % (10**9 + 7)
