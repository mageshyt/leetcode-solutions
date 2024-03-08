class Solution:
    # Time : O(n) | Space : O (1)
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        # loop until left pointer is less than right pointer and characters at both pointers are equal
        while left < right and s[left] == s[right]:
            # temporary variable to store the current character
            tmp = s[left]

            # move left pointer towards right as long as characters are equal to the temporary character
            while left <= right and s[left] == tmp:
                left += 1
                
            # move right pointer towards left as long as characters are equal to the temporary character
            while right >= left and s[right] == tmp:
                right -= 1

        # calculate the length of the substring
        return right - left + 1
