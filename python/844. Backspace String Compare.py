from inspect import stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backSpace(string):
            stack = []
            for char in string:
                if char =='#':
                    if stack: # is tack is not empty
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)

        return backSpace(s) == backSpace(t)
if __name__ == '__main__':
    s=Solution()
    print(s.backspaceCompare("ab#c", "ad#c"))
    print(s.backspaceCompare("a##c", "#a#c"))
    print(s.backspaceCompare("a#c", "b"))
