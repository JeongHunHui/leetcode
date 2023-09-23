class Solution:
    def trap(self, height: List[int]) -> int:
        answer, max_h, idx_list = 0, 0, []
        for i, h in enumerate(height):
            if max_h == h:
                idx_list.append(i)
            elif max_h < h:
                max_h = h
                idx_list = [i]
        
        c_max_h = -1
        for h in height[:idx_list[0]]:
            if h > c_max_h:
                c_max_h = h
            else:
                answer += c_max_h - h
        
        c_max_h = -1
        for h in height[idx_list[-1]+1:][::-1]:
            if h > c_max_h:
                c_max_h = h
            else:
                answer += c_max_h - h

        for h in height[idx_list[0]+1:idx_list[-1]]:
            answer += max_h - h

        return answer
            