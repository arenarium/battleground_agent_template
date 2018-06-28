from battleground.agent import Agent


class MyPersistentAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_turn_num = None
        self.default_mem = {"guess": 5}

    def move(self, state):
        memory = self.get_memory(default=self.default_mem)
        # print(memory)
        self.my_turn_num = state["turn"]
        return {"value": memory["guess"]}

    def observe(self, state):
        memory = self.get_memory(default=self.default_mem)
        # after initialization or if something made it forget:
        self.set_memory(memory)
        # implementing temporal-difference learning:
        # if last turn was my turn
        if state["turn"] - 1 == self.my_turn_num:
            last_roll = state["last_roll"]
            delta = last_roll - memory["guess"]
            # improve guess based on last roll data
            memory["guess"] += delta * 0.01
            self.set_memory(memory)
