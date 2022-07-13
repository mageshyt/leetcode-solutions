'''Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
'''





from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words, k: int) :
        counter = Counter(words)
        #by default we have min heap in python so we need to change it to max heap by using -x
        heap=[(-count,word) for word,count in counter.items()]

        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
if __name__ == '__main__':
    s=Solution()
    print(s.topKFrequent(["i","love","leetcode","i","love","coding"], 2))
    print(s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))