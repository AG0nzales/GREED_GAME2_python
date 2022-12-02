from game.shared.color import Color
from game.shared.point import Point


class Actor:
    # A visible, moveable thing that participates in the game. 
    
    # The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    # space.

    # Attributes:
    #     _text (string): The text to display
    #     _font_size (int): The font size to use.
    #     _color (Color): The color of the text.
    #     _position (Point): The screen coordinates.
    #     _velocity (Point): The speed and direction.
    

    def __init__(self):

        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
       


    def get_color(self):

        return self._color

    def get_font_size(self):

        return self._font_size

    def get_position(self):

        return self._position
    
    def get_text(self):

        return self._text

    def get_velocity(self):

        return self._velocity
    
    def move_next(self, max_x, max_y):

        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):

        self._color = color

    def set_position(self, position):

        self._position = position
    
    def set_font_size(self, font_size):

        self._font_size = font_size
    
    def set_text(self, text):

        self._text = text

    def set_velocity(self, velocity):

        self._velocity = velocity