class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = str(bin(x))[2::]
        y_bin = str(bin(y))[2::]
        ham = 0
        bin_len_diff = len(y_bin) - len(x_bin)
        if bin_len_diff > 0:
            x_bin = '0'*(len(y_bin) - len(x_bin)) + x_bin
        elif bin_len_diff < 0:
            y_bin = '0'*(len(x_bin) - len(y_bin)) + y_bin
        for j in range(len(x_bin)):
            if x_bin[j] != y_bin[j]:
                ham += 1
        return ham

test = Solution()
print(test.hammingDistance(14, 4))