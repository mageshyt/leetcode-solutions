class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string,int>map;
        int maxLength = 0;
        for(auto& word : words) {
          string reversedWord = word;
          reverse(reversedWord.begin(), reversedWord.end());

          // check if the reversed word exists in the map 
          if(map[word]>0){
            maxLength += 4; // each pair contributes 4 to the length
            map[word]--;
          } else {
            map[reversedWord]++;
          }
        }

        // check for the center word
        for(auto& entry : map) {
            if(entry.first[0] == entry.first[1] && entry.second > 0) {
                maxLength += 2; // one center word contributes 2 to the length
                break; // only one center word can be used
            }
        }

        return maxLength;
    }
};
