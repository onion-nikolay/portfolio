class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def rotated(N):
            s_N = str(N)
            to_replace = {'0': '0', '1': '1', '2': '5', '3': 'a', '4': 'a',
                          '5': '2', '6': '9', '7': 'a', '8': '8', '9': '6'}
            new_s_N = ''.join([to_replace[ch] for ch in s_N])
            try:
                new_N = int(new_s_N)
            except ValueError:
                return 0
            if new_N == N:
                return 0
            else:
                return 1

        return sum(list(map(rotated, range(1, N + 1))))

sol = Solution()
