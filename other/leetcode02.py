class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        alphabet = set(map(chr, range(ord('a'), ord('z')+1)))
        new_alphabet = dict()
        for number, ch in enumerate(S):
            new_alphabet[ch] = number
        for number, ch in enumerate(alphabet - set(new_alphabet.keys())):
            new_alphabet[ch] = len(S) + number
        counter = dict()
        for _key in new_alphabet.keys():
            counter[_key] = 0
        for ch in T:
            counter[ch] += 1
        result = ''
        for _key in new_alphabet.keys():
            result += _key * counter[_key]
        return result

sol = Solution()
sol.customSortString('fabcd', 'cccbbbaaafgh')
