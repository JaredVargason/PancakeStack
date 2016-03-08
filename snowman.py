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

def tokenize(line)
	tokens = []	
	word = ""
	for (c in line):
		if  
		
		
#Returns the type of a line  
def getLineType(line): 
	

def interpret(line):
	int line_type = getLineType(line)

	if line_type == 0:	#exit
		print("user exit")
		sys.exit(0)

	elif line_type == 1: #variable creation or assignment
		print("new")			
	
	elif line_type == 2: #push 
			
	
	elif line_type == 3: #pop
	
#Run interactive shell
if (len(sys.argv) == 1):
	print("SNOWMAN SHELL VER 1.0\n")
	shell()
	
#Interpret script
elif (len(sys.argv) == 2):
	print("script")
			
else:  
	print ("usage: \"snowman.py\" for interactive shell OR\n\"snowman.py <FILENAME>\" for file interpretation")
