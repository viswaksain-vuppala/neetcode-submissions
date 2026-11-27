class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hm={}
        n=len(nums)

        for num in nums:
            hm[num] = hm.get(num,0) + 1

        m=0
        ans=None
        for key, count in hm.items():
            if count>m:
                m=count
                ans=key

        return ans


             
                

        