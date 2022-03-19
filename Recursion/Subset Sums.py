class Solution:
	def subsetSums(self, arr, N):
	    self.ResSum = []
	    def helper(arr,Start,End,subSum,subSet):
	        if(Start >= End):
	            self.ResSum.append(subSum)
	            return
	        subSet.append(arr[Start])
	        subSum += arr[Start]
	        helper(arr,Start+1,End,subSum,subSet)
	        subSet.pop()
	        subSum -= arr[Start]
	        helper(arr,Start+1,End,subSum,subSet)
	    helper(arr,0,N,0,[])
	    return self.ResSum
