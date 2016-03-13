MAX_EYES = 8

class Ball:

	def __init__(self):
		self.size = 0
		self.nose = False
		self.eyes = 0 #counter
		self.mouth = 0 #different styles.
		self.arms = 0 #make this flags.
		self.hat = 0 #different styles
		self.buttons = 0 #counter
	
	def add(self, item):
		if item == 'nose':	
			pass	
		elif item == 'eyes': 
			pass	
		elif item == 'mouth': 
			pass	
		elif item == 'arm':
			pass
		elif item == 'hat':
			pass
		elif item == 'button':

	def remove(self):
		pass

class Snowman: #it's a stack, ok?

	def __init__(self):
		self.balls = []

	def push(self, item):
		if item.size < self.peek().size:
			self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def isEmpty(self):
		return self.items == [] 
	
	def size(self):
		return len(self.items)
	
	
