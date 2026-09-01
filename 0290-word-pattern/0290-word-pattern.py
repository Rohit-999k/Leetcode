class Solution(object):
    def wordPattern(self, pattern, s):
        w = s.split()
        if len(pattern) != len(w):
            return False

        c2w = {}
        w2c = {}

        for c, w in zip(pattern, w):
            if c in c2w and c2w[c] != w:
                return False

            if w in w2c and w2c[w] != c:
                return False

            c2w[c] = w
            w2c[w] = c
        return True