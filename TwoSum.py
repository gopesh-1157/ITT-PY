class Solution(object):
    def twoSum(self, nums, target):

        # Loop through each element in the list
        for i in range(len(nums)):
            
            # Check every next element after i
            for j in range(i + 1, len(nums)):
                
                # If the sum of two numbers equals the target
                if nums[i] + nums[j] == target:
                    
                    # Return the indices of the two numbers
                    return i, j
