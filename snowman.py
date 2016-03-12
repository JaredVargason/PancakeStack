import sys
from stringFunctions import tokenize

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

		
		
'''Returns the type of a line  
EXIT: 0
VARIABLE DECLARATION: 1
'''
def getLineType(tokens): 
	if len(tokens) == 1: #exit	
		return 0
	if len(tokens) == 2: #variable declaration
		return 1
	return -1	

def interpret(line):
	tokens = tokenize(line)
	line_type = getLineType(tokens)
	print("LINE TYPE:", line_type)

	if line_type == 0:	#exit
		print("user exit, closing shell")
		sys.exit(0)

	elif line_type == 1: #variable declaration 
		if (tokens[1] in snowman_dict or tokens[0] in ball_dict):	
			print(tokens[0], "already declared")
		
		if (tokens[0] == 'ball'):	
			ball_dict[tokens[0]] = 			

		else: 
			snowman_dict[tokens[0]]	= snowman_construct
	
	elif line_type == 2: #push 
		pass		
	
	elif line_type == 3: #pop
		pass
	
#Run interactive shell
if (len(sys.argv) == 1):
	print("SNOWMAN SHELL VER 1.0\n")
	shell()
	
#Interpret script
elif (len(sys.argv) == 2):
	print("script")
			
else:  
	print ("usage: \"snowman.py\" for interactive shell OR\n\"snowman.py <FILENAME>\" for file")
