


def Solution():

    user_choice = input().upper()

    letters=[]

    for i in range(65,ord(user_choice)+1):
        letters.append(chr(i))


    # Dim pattern as String
    for i in range(len(letters)):
        gap=(i+1)*' '
        l=[]
        if i ==0:
            l.append('')
        for j in range(i+1):
            if(j==i or j==0):
                l.append(letters[i])
            else:
              l.append('')
            
                 #
        if i ==0:
            l.append('')
        print(l)
Solution()