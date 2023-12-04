class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=0
        good_count=0

        left=0

        while (left<len(num)):
            right=left+1


            while(right < len(num) and (right-left <3) and num[left]==num[right]):
               right+=1

            if right-left>=3:
                # print("current ",num[left:right])
                res=max(res,int(num[left:right]))
                good_count+=1
                # print("res",res)
            left=right
           
           

        return str(res) if res!=0 else "000" if good_count>0 else ""
    


if __name__ == '__main__':
    num="6777133339"
    print(Solution().largestGoodInteger(num))