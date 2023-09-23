class Solution:
    def trap(self, height: List[int]) -> int:
        # 가장 높은 곳들의 index들을 구함
        # 가장 높은 곳이 | 라고하면
        # [ 왼쪽 > 높은 곳 탐색 -> | 중간 부분 탐색 -> | <- 오른쪽 > 높은 곳 탐색 ]

        # 가장 높은 곳의 높이와 그 곳의 인덱스를 구함
        answer, max_h, l_max_i, r_max_i = 0, -1, -1, -1
        for i, h in enumerate(height):
            if max_h == h:
                r_max_i = i
            elif max_h < h:
                max_h = h
                l_max_i = i
                r_max_i = i
        print(max_h, l_max_i, r_max_i)

        # 왼쪽부터 가장 높은 곳 까지 탐색
        c_max_h = -1
        for h in height[:l_max_i]:
            if h > c_max_h:
                c_max_h = h
            else:
                answer += c_max_h - h
        
        # 오른쪽부터 가장 높은 곳 까지 탐색
        c_max_h = -1
        for h in height[r_max_i+1:][::-1]:
            if h > c_max_h:
                c_max_h = h
            else:
                answer += c_max_h - h

        # 가장 높은 곳들 사이에 있는 곳 탐색
        for h in height[l_max_i+1:r_max_i]:
            answer += max_h - h

        return answer
            