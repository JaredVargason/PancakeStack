def validChar(c):
	return (c >= '0' and c <= '9') or (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

def tokenize(line):
	tokens = []	
	word = ""
	
	for c in line:
		if validChar(c):
			word = word + c 
		elif c == ' ':
			if (word):
				tokens.append(word)
				word = ""
		elif c == '(' or c == ')' or c == ',' or c == '=':  
			if (word):
				tokens.append(word)
				word = ""
			tokens.append(c)

	#add last word
	if (word):
		tokens.append(word)

	return tokens
