from battleground.agent import Agent
from battleground.games.arena import building_blocks


class ArenaAgent(Agent):

    def move(self, state):
        """
        Attack yourself.
        """
        move = building_blocks.attack(state, state['current_player'])
        # try attack move is valid
        if move is not None:
            return move

        # if move is not possible, do nothing.
        return {}
