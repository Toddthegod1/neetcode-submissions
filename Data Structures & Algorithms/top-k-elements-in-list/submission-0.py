class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count how many times each number appears
        count = {}
        # freq[i] will store a list of numbers that appear exactly i times
        # We make len(nums) + 1 buckets because the max frequency a number can have
        # is the length of nums (e.g., [1,1,1,1] → freq[4] contains 1)

        freq = [[] for i in range(len(nums) + 1)]
         
         # Count the frequency of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Place each number into the bucket matching its frequency
        for n, c in count.items():
            freq[c].append(n) # number n (number) appears c (count) times

        res = [] # This will store the top k frequent numbers

        # Loop through the buckets starting from the highest frequency
        # i goes from len(freq)-1(last index) down to 1
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:  # Look at all numbers with frequency i
                res.append(n)  # Add them to the result
                if len(res) == k: # Stop once we have k numbers
                    return res


            
            