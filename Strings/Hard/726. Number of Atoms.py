"""Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

"""

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # 1. we are going to use stack of dictionaries to keep track of the counts of the atoms

        stack = [defaultdict(int)]

        # 2. we are going to use a pointer to iterate over the formula
        i = 0
        size=len(formula)

        while i < size:
            # if '(' is found, we are going to push a new dictionary to the stack
            if formula[i] == '(':
                stack.append(defaultdict(int))

            elif formula[i]==")":
                curr_map=stack.pop()
                count=0
                while i+1 < size and formula[i+1].isdigit():
                    count=count*10+int(formula[i+1])
                    i+=1

                count=max(1,count)


                for ele in curr_map:
                    stack[-1][ele]+=curr_map[ele]*count

            else:
                ele=formula[i]
                # if the next character is lowercase, we are going to append it to the element
                if i+1 < size and formula[i+1].islower():
                    ele+=formula[i+1]
                    i+=1

                # we are going to get the count of the element
                count=0

                while i+1 < size and formula[i+1].isdigit():
                    count=count*10+int(formula[i+1])
                    i+=1

                # if the count is 0, we are going to set it to 1

                count=max(1,count)

                # we are going to update the count of the element in the top dictionary of the stack

                stack[-1][ele]+=count

            i+=1


        # 3. we are going to merge the dictionaries in the stack
        res=""
        for ele in sorted(stack[0].keys()):
            res+=ele
            if stack[0][ele]>1:
                res+=str(stack[0][ele])

        return res


print(Solution().countOfAtoms("H2O")) # "H2O"
print(Solution().countOfAtoms("Mg(OH)2")) # "H2MgO2"


