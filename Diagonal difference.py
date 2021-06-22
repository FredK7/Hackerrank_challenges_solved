def diagonalDifference(arr):
    # Write your code here
    s=[]
    p=0
    k=0
    h=0
    s_r=0
    for l in range(len(arr)):
        s_r+=arr[l][l]
#print('s_r=' + str(s_r))
    for i in reversed(arr):
        s.extend([i])
    for j in range(len(s)):
            k=len(s)
            p+=s[j][j]
    return(abs(s_r-p))
