class Solution:
    def intToRoman(self, num: int) -> str:
        roman_datas = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
        c_roman, c_num = roman_datas[0]
        point = 0
        answer = ''
        while num > 0:
            if c_num > num:
                point += 1
                c_roman, c_num = roman_datas[point]
            else:
                num -= c_num
                answer += c_roman
        return answer