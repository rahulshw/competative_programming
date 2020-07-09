# Problem: https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/

import copy


class Solution:
    def prisonAfterNDays(self, cells, N):
        if N == 0:
            return cells

        # getting rid of first special case and last two digits
        _old_cells = self.play(cells)

        period = self.find_periodicity_of_states(_old_cells)
        _N = (N-1) % period

        new_cells = _old_cells
        for i in range(_N):
            new_cells = self.play(new_cells)

        return new_cells

    def find_periodicity_of_states(self, _old_cells):
        """ will be non crossing periodic because there is only one way from each state """
        max_period = 64 # 2**6
        all_states = dict()
        new_cells = _old_cells
        for i in range(max_period):
            new_cells = self.play(new_cells)
            key = ''.join(map(str, new_cells))
            if key in all_states:
                period = i
                return period
            else:
                all_states[key] = None

    def play(self, old_cells):
        new_cells = copy.deepcopy(old_cells)
        new_cells[0] = 0
        new_cells[-1] = 0
        for i in range(1, 7):
            if old_cells[i - 1] == old_cells[i + 1]:
                new_cells[i] = 1
            else:
                new_cells[i] = 0
        return new_cells


if __name__ == '__main__':
    s = Solution()

    cells = [int(x) for x in list('01011001')]
    cells = [1,0,0,1,0,0,1,0]
    N = 1000000000
    print(s.prisonAfterNDays(cells, N))

