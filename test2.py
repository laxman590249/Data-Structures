class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre - 1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre
        print(lps)

        # Main algorithm
        n = 0  # needle index
        for h in range(len(haystack)):
            print('B', h, n)
            while n > 0 and needle[n] != haystack[h]:
                print('I', needle[n], haystack[h], lps, n, lps[n-1])
                n = lps[n - 1]
            print('A', h, n)
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1


print(Solution().strStr('sadbutsadbutbutbutpbut', 'butbutbutbut'))