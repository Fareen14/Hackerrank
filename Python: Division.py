#Task
  #Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .
#You don't need to perform any rounding or formatting operations.

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print('{0} \n{1}'.format((a//b),(a/b)))

#Input (stdin)
4
3

#Your Output (stdout)
1
1.33333333333

#Expected Output
1
1.33333333333