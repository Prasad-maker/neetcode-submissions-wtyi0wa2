class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        visited = set(deadends)
        begin = {"0000"}
        end = {target}
        steps = 0

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit = digit = str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res
        queue = deque([("0000",0)])
        while begin and end:
            if len(begin)> len(end):
                begin,end = end, begin
            steps +=1
            temp = set()
            for lock in begin:
                for child in children(lock):
                    if child in end:
                        return steps
                    if child in visited:
                        continue
                    visited.add(child)
                    temp.add(child)
            begin = temp
        return -1



        