from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here!


class MoveActorsAction(Action):

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # 1) get all the actors from the cast

        all_actors = cast.get_all_actors()

        # 2) loop through the actors

        for snake in (all_actors):
            # 3) call the move_next() method on each actor
            snake.move_next()
