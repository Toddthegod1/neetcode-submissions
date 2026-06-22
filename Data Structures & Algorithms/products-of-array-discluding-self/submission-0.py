class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array 'res' with all 1s.
        # This will eventually hold the final product for each index.
        res = [1] * (len(nums))
        # -----------------------
        # FIRST PASS: Prefix product
        # -----------------------
        prefix = 1  # This variable keeps track of the product of all elements to the *left* of the current index.
        for i in range(len(nums)):
            # Before multiplying by nums[i], assign the current prefix to res[i].
            # res[i] = product of all elements before index i.
            res[i] = prefix
            # Update prefix by multiplying it with the current number.
            # So in the next iteration, prefix represents the product of all numbers up to nums[i].
            prefix *= nums[i]
        # -----------------------
        # SECOND PASS: Postfix product
        # -----------------------
        postfix = 1 # Keeps track of the product of all elements to the *right* of the current index.
         # Traverse the array backward
        for i in range(len(nums) -1, -1, -1):
            # Multiply the current res[i] (which already has the prefix product)
            # by the postfix (product of all elements to the right of i).
            res[i] *= postfix
             # Update postfix by multiplying with the current number.
            # So next iteration will use the product of everything to the right of the next element.
            postfix *= nums[i]
        return res

