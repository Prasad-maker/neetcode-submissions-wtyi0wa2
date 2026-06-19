class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        count = Counter(hand)
        for num in sorted(count):
            cur = count[num]
            while count[num]:

                for i in range(num,num+groupSize):
                    if count[i]<cur:
                        return False
                    count[i]-=cur
        return True 
        