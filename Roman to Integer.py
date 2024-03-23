class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900,
        }
        num_list=[s[0]]
        prev=s[0]
        i=1
        while(i<len(s)):
            if(prev+s[i] in num_dict.keys()):
                if  prev:
                    num_list[-1]=prev+s[i]
                    prev=''
                else:
                    num_list.append(s[i])
                    prev=s[i]
            else:
                num_list.append(s[i])
                prev=s[i]  
            i+=1


        num_list=[num_dict[i] for i in num_list]

        return sum(num_list)