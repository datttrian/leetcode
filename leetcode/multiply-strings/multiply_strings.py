class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total_sum = mul + pos[p2]
                quotient, remainder = divmod(total_sum, 10)
                pos[p1] += quotient
                pos[p2] = remainder

        result = "".join(map(str, pos)).lstrip("0")
        return result if result else "0"
