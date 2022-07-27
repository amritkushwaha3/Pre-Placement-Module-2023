class Solution(object):
    def findAnagrams(self, s, p):

        pc = collections.Counter(p)
        slice_str = s[: len(p)]
        sc = collections.Counter(slice_str)

        slice_index = []

        for x in range(0, len(s) - len(p) + 1):
            if x > 0:
                sc[s[x - 1]] -= 1
                sc[s[x + len(p) - 1]] += 1

                if sc[s[x - 1]] == 0:
                    del sc[s[x - 1]]

            if len(sc) == len(pc):
                if sc == pc:
                    slice_index.append(x)

        return slice_index