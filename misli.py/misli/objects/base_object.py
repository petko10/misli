class BaseObject():
    def __init__(self, **state):
        state.setdefault('id', id(self))
        state.setdefault('data', {})

        self.__state_keys = []
        self.id = 0
        self.data = {}

        self.add_state_keys(state.keys())
        self.set_state(**state)

    def add_state_keys(self, keys):
        self.__state_keys.extend(keys)

    def state(self):
        self_state = {}
        for k, v in self.__dict__.items():
            if k in self.__state_keys:
                self_state[k] = v

        return self_state

    def set_state(self, **state):
        filtered = {k: state[k] for k in state if k in self.__state_keys}

        self.__dict__.update(filtered)