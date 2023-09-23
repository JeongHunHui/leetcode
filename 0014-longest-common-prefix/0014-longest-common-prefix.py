class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_s, last_s, answer = strs[0], strs[-1], ''
        for i in range(min(len(first_s),len(last_s))):
            if first_s[i] != last_s[i]:
                break
            answer += first_s[i]
        return answer