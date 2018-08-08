from battleground.agent import Agent
from battleground.games.arena import building_blocks
import numpy as np


class ArenaAgent(Agent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.threshold = None

    def move(self, state):
        """
        Attack nearest other or move towards nearest other.
        """

        memory = self.get_memory(default={'thresholds': [2]*23})
        self.my_player_index = state['current_player']

        thresholds = memory['thresholds']

        # initialize threshold on first game
        if self.threshold is None:
            if np.random.uniform() > .8:
                self.threshold = np.random.randint(0, 23)
            else:
                self.threshold = int(np.argmax(thresholds))

        my_health = building_blocks.my_hitpoints(state)
        closest = building_blocks.closest_other_location(state)

        if my_health > self.threshold:

            # try attack move is valid
            move = building_blocks.attack_closest(state)
            if move is not None:
                return move

            # if attack is not possible, move towards closest other
            move = building_blocks.move_toward(state, closest)
            if move is not None:
                return move

        else:
            # if health is low, run away from closest other
            move = building_blocks.move_away(state, closest)

        # if move is not possible, do nothing.
        return {}

    def observe(self, state):
        # at the end of each game, we will update game state values
        if state['game_over'] == 'True':
            if self.my_player_index is not None:
                # get my score
                scores = state['scores']
                my_score = scores[self.my_player_index]

                # get memory
                memory = self.get_memory(default={'thresholds': [2]*23})
                thresholds = memory['thresholds']

                # update value for threshold using learning rate
                thresholds[self.threshold] = thresholds[self.threshold] * .9 + 0.1*my_score
                print([round(x, 2) for x in thresholds])

                # save my memory and reset state
                self.set_memory({'thresholds': thresholds})
                self.threshold = None
