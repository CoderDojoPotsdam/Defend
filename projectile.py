class Projectile(object):
	def __init __(ptype,damage,texture):
		self.__texture = texture
		self.__type = ptype
		self.__motion = [0,0]
		self.__damage = damage
		
