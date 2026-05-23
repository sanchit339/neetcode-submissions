class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res : List[List[str]] = []
        tmp : List[tuple(str , str)] = []
        for _ in strs:
            tmp.append((''.join(sorted(_)) , _ )) 
        tmp.sort(key = lambda x : x[0])
        lst : List[str] = []
        i = len(strs) - 1
        start = tmp[i][0]
        while(i >= 0):
            curr = tmp[i][0]
            to_append = tmp[i][1]
            if curr == start:
                lst.append(to_append)
            else :
                start = curr
                res.append(lst) #takes exactly one argument (0 given)
                lst = []
                lst.append(to_append)
            i -= 1
        res.append(lst)
        return res