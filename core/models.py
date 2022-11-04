class Ball:
	def __init__(self):
		self.color: str = ''
		self.circ: float = 0.0
		self.material: str = ''

	def change_color(self, color: str):
		self.color = color
		return self.color

	def show_color(self):
		return self.color


class Square:
	def __init__(self):
		self.size: float = 0.0

	def change_size_value(self, value: float):
		self.size = value
		return self.size

	def show_size_value(self):
		return self.size

	def calc_area(self):
		return self.size ** 2
