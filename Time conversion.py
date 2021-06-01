#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    w=str(s)
    v=''
    m=''
    y=''
    t=0
    z=''
    u=''
    mid_night=0
    mid_night_time=''
    if w.endswith('AM')==True:
        m=w.replace('AM','')
        #return(m)
        mid_night=int(m[0]+m[1])+12
        if mid_night==24:
            mid_night_time=m.replace(m[0]+m[1],'00')
            return(mid_night_time)
        return(m)
            
        #return(m)
    if w.endswith('PM')==True:
        u=w.replace('PM','')
        t=int(w[0]+w[1])+12
        z=str(t)
        if t==24:
            y='12'
            v=u.replace(w[0]+w[1], y)
            return(v)
        v=u.replace(w[0]+w[1], z)    
        return(v)

   
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
