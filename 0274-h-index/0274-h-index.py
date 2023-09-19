class Solution:
    def hIndex(self, citations: List[int]) -> int:
        answer = 0
        citations.sort(reverse=True)
        for c in citations:
            if c > answer:
                answer += 1
            else:
                break
        return answer