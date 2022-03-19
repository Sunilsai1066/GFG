#User function Template for python3

class Solution:
    def subsets(self, A):
        FinRes = []
        Start,End = 0,len(A)-1
        def subSets(Lis,Res,Start,End,FinRes):
            if(Start > End):
                FinRes.append(Res[:])
                return
            Res.append(Lis[Start])
            subSets(Lis,Res,Start+1,End,FinRes)
            Res.pop()
            subSets(Lis,Res,Start+1,End,FinRes)
        subSets(A,[],Start,End,FinRes)
        FinRes.sort()
        return FinRes
