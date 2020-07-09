class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        count_of_ones = 0
        while z != 0:
            _t = z>>1
            h = z/2
            z = _t
            if _t != h:
                count_of_ones +=1
        return count_of_ones


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1,4))