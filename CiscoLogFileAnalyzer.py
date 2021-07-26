string1 = 'trace'
TraceCounter = 0

# opening a text file
file1 = open("ciscofile.log", "r")

# read file content
readfile = file1.read()

# seeing how many times "trace" is in the file
def countTrace():
	global TraceCounter

	for string1 in readfile:
		TraceCounter += 1
		

countTrace()

print(TraceCounter)

# closing a file
file1.close()
