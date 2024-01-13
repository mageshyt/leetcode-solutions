class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        # flag for e and point
        ponitSeen=False
        # flag for number
        eSeen=False
        # flag for number after e
        numberSeen=False

        # replace E with e
        s=s.replace('E','e')

        for i in range(len(s)):
            curr=s[i]
            # if curr is number
            if curr.isdigit():
                numberSeen=True

            # if curr is e
            elif curr=='e' or curr=='E':
                # if e is already seen or number is not seen
                if eSeen or not numberSeen:
                    return False
                # if e is not seen so make eSeen=True
                eSeen=True
                # reset numberSeen because we need to check number after e
                numberSeen=False

            # if curr is point
            elif curr=='.':
                # if point is already seen or e is already seen
                if ponitSeen or eSeen:
                    return False
                # if point is not seen so make pointSeen=True
                ponitSeen=True

            # if curr is + or -
            elif curr=='+' or curr=='-':
                # if curr is not first char or prev char is not e
                if i!=0 and s[i-1]!='e':
                    return False
                
            # if curr is not valid
            else:
                return False
            
        return numberSeen
    


