from battleground.agent import Agent
from battleground.games.arena import building_blocks


class ArenaAgent(Agent):

    def move(self, state):
        """
        Attack if healthier that others, run otherwise.
        """

        others_health = building_blocks.others_hitpoints(state)

        my_health = building_blocks.my_hitpoints(state)

        closest = building_blocks.closest_other_location(state)

        if my_health > min(others_health.values()):

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
