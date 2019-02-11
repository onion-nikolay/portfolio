class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        length = max(len(a), len(b)) + 1
        s1 = [0] * (length - len(a)) + list(map(int, list(a)))
        s2 = [0] * (length - len(b)) + list(map(int, list(b)))
        s3 = [a + b for a, b in zip(s1, s2)]
        for index in range(length):
            real_index = length - index - 1
            s3[real_index-1] += s3[real_index] // 2
            s3[real_index] = s3[real_index] % 2
        if s3[0] == 0:
            return ''.join(map(str, s3[1:]))
        else:
            return ''.join(map(str, s3))

print(Solution().addBinary('111', '111'))
