class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        left_smaller = [0] * n
        left_larger = [0] * n
        right_smaller = [0] * n
        right_larger = [0] * n

        for j in range(n):
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller[j] += 1
                elif rating[i] > rating[j]:
                    left_larger[j] += 1

        for j in range(n):
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller[j] += 1
                elif rating[k] > rating[j]:
                    right_larger[j] += 1

        num_teams = 0
        for j in range(n):
            num_teams += left_smaller[j] * right_larger[j] + left_larger[j] * right_smaller[j]

        return num_teams