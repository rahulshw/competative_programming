class Solution:
    maps = {}

    def maxlen(self, a, b):
        if len(a) > len(b):
            return a
        else:
            return b

    def longestPalindrome(self, s: str) -> str:
        # print(s)
        if s in self.maps:
            return self.maps[s]
        if len(s) <= 1:
            return s
        if s[0] == s[-1]:
            _s = self.longestPalindrome(s[1:-1])
            if len(_s) + 2 == len(s):
                self.maps[s] = s
                return s
            else:
                ans = self.maxlen(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]))
                self.maps[s] = ans
                return ans
        else:
            ans = self.maxlen(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]))
            self.maps[s] = ans
            return ans

if __name__ == '__main__':
    import time
    s = Solution()
    string = "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
    time_start = time.time()
    res = s.longestPalindrome(string)
    time_end = time.time()
    print(res, time_end-time_start)