#Task  
# Read two integers from STDIN and print three lines where:
    #1.The first line contains the sum of the two numbers.
	#2.	The second line contains the difference of the two numbers (first - second).
	#3.	The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print('{0} \n{1} \n{2}’.format((a+b),(a-b),(a*b)))

#Input (stdin)
3
2

#Your Output (stdout)
5
1
6

#Expected Output
5
1
6
