from math import perm


def permutation(s,ans):
    if(len(s)==0):
        print(ans)
    
    for i in range (0,len(s)):
        ch=s[i]
        ros=s[0:i]+s[i+1:]
        permutation(ros,ans+ch)

permutation("RAVI","")