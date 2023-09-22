class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        status = ''
        up, down, check = 0, 0, 0
        arr = []
        candy_list = [1]*n
        for i in range(1,n):
            pre, cur = ratings[i-1], ratings[i]
            # 상승
            if pre < cur:
                if status == 'u':
                    up += 1
                else:
                    if down > 0:
                        print(status, check, i-1)
                        arr.append((status, check, i-1))
                    check = i-1
                    status = 'u'
                    up, down = 1, 0
            # 하락
            elif pre > cur:
                if status == 'd':
                    down += 1
                else:
                    if up > 0:
                        print(status, check, i-1)
                        arr.append((status, check, i-1))
                    check = i-1
                    status = 'd'
                    up, down = 0, 1
            # 유지
            elif status != 's':
                print('stay', status, check, i-1)
                arr.append((status, check, i-1))
                status = 's'
                up, down = 0, 0
        
        if status in 'ud':
            print(status, check, n-1)
            arr.append((status, check, n-1))
        
        print(arr)
        arr.sort(key=lambda x: x[2]-x[1])

        for status, start, end in arr:
            c = 1
            if status == 'u':
                for i in range(start, end+1):
                    candy_list[i] = c
                    c += 1
            else:
                for i in range(end, start-1, -1):
                    candy_list[i] = c
                    c += 1
        print(candy_list)
        return sum(candy_list)