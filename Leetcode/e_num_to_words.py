# Problem: https://leetcode.com/problems/integer-to-english-words/


class Solution:
    def numberToWords(self, num: int) -> str:
        print(num)
        data = {
            1000000000: 'Billion',
            1000000: 'Million',
            1000: 'Thousand',
            100: 'Hundred',
            90: 'Ninety',
            80: 'Eighty',
            70: 'Seventy',
            60: 'Sixty',
            50: 'Fifty',
            40: 'Forty',
            30: 'Thirty',
            20: 'Twenty',
            19: 'Nineteen',
            18: 'Eighteen',
            17: 'Seventeen',
            16: 'Sixteen',
            15: 'Fifteen',
            14: 'Fourteen',
            13: 'Thriteen',
            12: 'Twelve',
            11: 'Eleven',
            10: 'Ten',
            9: 'Nine',
            8: 'Eight',
            7: 'Seven',
            6: 'Six',
            5: 'Five',
            4: 'Four',
            3: 'Three',
            2: 'Two',
            1: 'One',
            0: 'Zero'

        }
        if num<100 and num in data:
            return data[num]

        predef_nums = list(data.keys())[0:-1]
        words = []
        special_words = list(data.keys())[0:4]
        for predef_num in predef_nums:
            count = 0
            while num >= predef_num:
                count += 1
                num -= predef_num
            if count > 0:
                if predef_num >= 100:
                    words.append(self.numberToWords(count))
                words.append(data[predef_num])

        return ' '.join(words)


if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(1000))
