string1 = 'trace'
TraceCounter = 0

# opening a text file
file1 = open("ciscofile.log", "r")

# read file content
readfile = file1.read()

# checking condition for string found or not
def countTrace():
	global TraceCounter

	for string1 in readfile:
		TraceCounter += 1
		
	#else:
		#print('String', string1 , 'Not Found')

countTrace()

print(TraceCounter)

# closing a file
file1.close()
