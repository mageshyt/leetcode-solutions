  miss_count=0

        for i  in range(len(result)):
            if result[i] == "":
                result[i] = sorted_vowels[miss_count]
                miss_count+=1
