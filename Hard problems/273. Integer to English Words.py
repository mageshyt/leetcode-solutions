class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        big_scale = ["", "Thousand", "Million", "Billion"]
        result = ""
        scale_index = 0

        while num > 0:
            if num % 1000 != 0:
                result = self.convertToWords(num % 1000) + big_scale[scale_index] + " " + result
            num //= 1000
            scale_index += 1

        return result.strip()

    def convertToWords(self, num: int) -> str:
        if num == 0:
            return ""

        digit_string = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teen_string = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        ten_string = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""

        if num >= 100:
            result += digit_string[num // 100] + " Hundred "
            num %= 100

        if num >= 20:
            result += ten_string[num // 10] + " "
            num %= 10

        if num >= 10:
            result += teen_string[num - 10] + " "
        elif num > 0:
            result += digit_string[num] + " "

        return result



s = Solution()
print(s.numberToWords(123))
