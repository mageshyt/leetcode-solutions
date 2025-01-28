class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # conver to binary
        bin1=bin(num1)[2:]
        bin2=bin(num2)[2:]

        bin1OneCount=bin1.count("1")
        bin2OneCount=bin2.count("1")

        bin1=bin1.zfill(max(len(bin1),len(bin2)))
        bin2=bin2.zfill(max(len(bin1),len(bin2)))

        ans=[]

        for i in range(len(bin1)):
            if bin1[i] == '1' and bin2OneCount>0:
                ans.append('1')
                bin2OneCount-=1
            else:
                ans.append('0')


        i=len(ans)-1

        while bin2OneCount>0:
            if ans[i] != '1':
                ans[i]='1'
                bin2OneCount-=1
            i-=1

        return int("".join(ans),2)


s=Solution()
num1 = 3
num2 = 5
print(s.minimizeXor(num1,num2))
num1 = 1
num2 = 12
print(s.minimizeXor(num1,num2))
    
