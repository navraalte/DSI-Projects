n = int(raw_input())
input = [  raw_input().split() for x in range(0,n) ]
print input 
for i in range(0,n):
	try: print(int(input[i][0])/int(input[i][1]))
	except ZeroDivisionError as e:
		print "Error Code:",e
	except ValueError as e:
		print "Error Code:",e