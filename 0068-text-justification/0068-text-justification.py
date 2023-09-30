import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        arr = []
        s = words[0]
        for i in range(1, len(words)):
            word = words[i]
            print(s, i,word)
            l = len(s)
            cl = len(word)
            print(l + cl + 1 <= maxWidth)
            if l + cl + 1 <= maxWidth:
                s += ' ' + word
            else:
                s_arr = s.split()
                # 공백 수
                blank = len(s_arr) - 1
                # 필요한 전체 공백 수
                blank_count = maxWidth - l + blank
                if blank == 0:
                    arr.append(s+' '*blank_count)
                    s = word
                    continue
                # 한 공백당 칸 수
                blank_avg = blank_count // blank
                blank_left = blank_count % blank
                answer = ''
                if blank_left == 0:
                    answer = (' '*blank_avg).join(s_arr)
                else:
                    for i in range(blank_left):
                        answer += s_arr[i] + ' '*(blank_avg+1)
                    for i in range(blank_left, blank):
                        answer += s_arr[i] + ' '*blank_avg
                    answer += s_arr[-1]
                arr.append(answer)
                s = word
        arr.append(s+' '*(maxWidth-len(s)))
        return arr