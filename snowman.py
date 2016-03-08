import sys

#variable maps
snowman_dict = {}
ball_dict = {}

def shell():
	while (True):
		command = input("snowman > ")	
		interpret(command)

def script():
	f = open(sys.argv[1], 'r')	
	for line in f:
		interpret(f)

	f.close()
		
#Returns the type of a line by 
def getLineType(line): #

def interpret(line):
	int line_type = getLineType(line)

	if line_type == 0:	#exit
		print("user exit")
		sys.exit(0)

	elif line_type == 1: #variable creation or assignment
		print("new")			
	
	elif line_type == 2: 
		
	
	elif line_type == 3:
	
#Run interactive shell
if (len(sys.argv) == 1):
	print("SNOWMAN SHELL VER 1.0\n")
	shell()
	
#Interpret script
elif (len(sys.argv) == 2):
	print("script")
			
else:  
	print ("usage: \"snowman.py\" for interactive shell OR\n\"snowman.py <FILENAME>\" for file interpretation")
