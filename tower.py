class Tower:
    def __init__(self):
		self.name = "Tower"
		self.__health = 100


	def update(self,*args):
		if args[0]=="hit":
			self.__health -=args[1]
			
		
