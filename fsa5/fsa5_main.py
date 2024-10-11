from enum import Enum

class State(Enum):
    Q0 = 0
    Q1 = 1
    Q2 = 2

class Q:
    def process(self, inpt: bool) -> tuple[State, int]:
        pass

class Q0(Q):
    def process(self, inpt: bool) -> tuple[State, int]:
        state = State.Q1 if not inpt else State.Q0
        return state, 0


class Q1(Q):
    def process(self, inpt: bool) -> tuple[State, int]:
        if not inpt:
            return State.Q2, 1
        return State.Q0, 0

class Q2(Q):
    def process(self, inpt: bool) -> tuple[State, int]:
        state = State.Q1 if not inpt else State.Q0
        return state, 0

class FSA:
    def __init__(self, instances: {State, Q}):
        self.instances = instances

    @staticmethod
    def instance():
        return FSA({State.Q0: Q0(), State.Q1: Q1(), State.Q2: Q2()})

    def process(self, input_data: [int]):
        input_data = list(map(lambda inpt: True if inpt == 1 else False, input_data))
        out = []
        current_state = self.instances[State.Q0]
        for input_datum in input_data:
            res = current_state.process(input_datum)
            out.append(res[1])
            current_state = self.instances[res[0]]
        return out