       print(uncommon_string)
        # left - right + 1
        for key, val in uncommon_string.items():
            ans += val[0]

        return ans
