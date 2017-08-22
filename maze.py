class Maze:
	def __init__(self, length=10, width=10, **kwargs):
		if not isinstance(length, int) or not isinstance(width, int):
			raise TypeError("Length and Width must be integers")
		if self.length < 1 or self.width < 1:
			raise ValueError("Length and Width must be at least equal to 1")