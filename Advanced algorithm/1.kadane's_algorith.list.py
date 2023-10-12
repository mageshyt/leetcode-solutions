
class KadansAlgorithm:

    # brute force approach

    def maxSubArrayBruteForce(self, nums: list[int]) -> int:
        max_sum = nums[0]
        iteration=0
        for i in range(len(nums)):

            for j in range(i, len(nums)):
                iteration+=1
                max_sum = max(max_sum, sum(nums[i:j+1]))
        return f"max_sum: {max_sum}, iteration: {iteration}"
    

    # Kadane's algorithm

    def maxSubArray(self, nums: list[int]) -> int:
        max_sum=nums[0]
        curr_sum=0

        iteration=0

        for num in nums:
            iteration+=1
            curr_sum=max(curr_sum,0)

            curr_sum+=num

            max_sum=max(max_sum,curr_sum)


        return f"max_sum: {max_sum}, iteration: {iteration}"
    


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(KadansAlgorithm().maxSubArrayBruteForce(nums))
    print(KadansAlgorithm().maxSubArray(nums))

