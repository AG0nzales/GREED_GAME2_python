from game.casting.actor import Actor
from game.shared.point import Point

class Artifact (Actor):
    def __init__(self):

        self._message = ""
        self._velocity = Point(0,1)

        super (). __init__ ()

    
