class Projectile(object):
	def __init __(ptype,damage,texture):
		self.__texture = texture
		self.__type = ptype
		self.__motion = [0,0]
		self.__damage = damage
		self.__position = [0,0]
	def update(self,*args):
		if args[0] == "move":
			for i in range (self.__position.len):
				self.__position[i] +=self.__motion[i]
