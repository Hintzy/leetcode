# TODO: Modify algorithm such that it only calculates the first range(n/2 + 1) numbers.  After which
#  uses list slicing to mirror the beginning of the list over the midpoint

class Solution:
    def generate(self, numRows):
        out = [[1]]
        if numRows == 1:
            return out
        for row in range(1, numRows+1)[1:]:
            current = [1]
            prev_row = out[row - 2]
            for index in range(1, row):
                if len(current) == row-1:
                    current.append(1)
                    out.append(current)
                    break
                next_val = prev_row[index - 1] + prev_row[index]
                current.append(next_val)
        return out


sol = Solution()
print(sol.generate(1))
print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(4))
print(sol.generate(5))
print(sol.generate(20))
