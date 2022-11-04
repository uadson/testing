from core.models import (
	Ball, Square
)

ball = Ball()
square = Square()

def test_change_color():
	assert ball.change_color(str) == str

def test_show_color():
	assert ball.show_color() == str


def test_change_size_value():
	value = 2
	assert square.change_size_value(value) == 2

def test_show_size_value():
	assert square.show_size_value()
