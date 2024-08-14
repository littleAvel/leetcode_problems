class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        # Initialize the dp table
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[1][0] = 1
        dp[1][1] = 1

        # Fill the dp table
        for i in range(2, n + 1):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]

        # Construct the strings from the dp table
        result = []