class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={}
        l = 0 
        freq = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            freq = max(freq, count[s[r]])

            while (r-l+1) - freq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
        return ans
        