
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # find the index of ch in word
        ch_idx=word.find(ch)
        # if ch is not in word
        if ch_idx==-1:
            return word

        prefix=word[:ch_idx+1][::-1] # reverse the prefix
        return prefix+word[ch_idx+1:] # return the reversed prefix and the rest of the word
