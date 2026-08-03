class Solution:
    def reorganizeString(self, s: str) -> str:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')]+= 1
        max_freq = max(count)
        if max_freq > (len(s)+1)//2:
            return ""
        res=""
        while len(res)<len(s):
            max_freq = count.index(max(count))
            res += chr(ord('a')+max_freq)
            count[max_freq]-=1
            tmp = count[max_freq]
            if len(res)==len(s):
                return res
            count[max_freq]=float("-inf")
            max_freq_2 = count.index(max(count))
            res += chr(ord('a')+max_freq_2)
            count[max_freq_2]-=1
            count[max_freq] = tmp
        return res

        
        
        