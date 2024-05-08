# Program
class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
            
search_insert = Solution()

nums_list = [1,3,5,6]
target_num = 5

# Call the removeElement method on the instance
result_length = search_insert.searchInsert(nums_list, target_num)

# Display the modified list and the new length
print("Target:", result_length)

