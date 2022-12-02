import random
from game.shared.point import Point
from game.casting.score import Score
class Director: 
    # The responsibility of a Director is to control the sequence of play.

    

    def __init__(self, keyboard_service, video_service):

        self._keyboard_service = keyboard_service
        self._video_service = video_service

        self._score=Score()
        
    def start_game(self, cast):

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):

        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):

        score = cast.get_first_actor("scores")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if robot.get_position().equals(artifact.get_position()):
                cast.remove_actor ("artifacts", artifact)
                

                if artifact.get_text()=='o':
                    score.subtract()
                elif artifact.get_text()=='*':
                    score.add()

                score.set_text (f"SCORE: {score.get_score()}")
                x = random.randint(1, 60 - 1)
                y = 1
                position = Point(x, y)
                position = position.scale(15)
                artifact.set_position(position)
                cast.add_actor('artifacts', artifact)

        
    def _do_outputs(self, cast):

        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
