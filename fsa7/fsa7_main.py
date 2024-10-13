from enum import Enum

class State(Enum):
    Q0 = 0
    Q1 = 1
    Q2 = 2
    Q3 = 3
    Q4 = 4

class Q:
    def process(self, inpt: bool) -> tuple[State, bool]:
        pass

class Q0(Q):
    def process(self, inpt: bool) -> tuple[State, bool]:
        if inpt:
            return State.Q2, None
        return State.Q1, None


class Q1(Q):
    def process(self, inpt: bool) -> tuple[State, bool]:
        if not inpt:
            return State.Q0, False
        return State.Q3, True

class Q2(Q):
    def process(self, inpt: bool) -> tuple[State, bool]:
        if inpt:
            return State.Q0, False
        return State.Q3, True

class Q3(Q):
    def process(self, inpt: bool) -> tuple[State, bool]:
        return State.Q4, True

class Q4(Q):
    def process(self, inpt: bool) -> tuple[State, bool]:
        return State.Q3, None

def int_to_bool(val: int) -> bool:
    if val == 1:
        return True
    elif val == 0:
        return False
    else:
        raise Exception(f'Only 1 and 0 are allowed, got {val}')

def bool_to_int(val: bool) -> int:
    if val:
        return 1
    elif not val:
        return 0
    else:
        raise Exception("None is not allowed")

class FSA:
    def __init__(self, instances: {State, Q}):
        self.instances = instances

    @staticmethod
    def instance():
        return FSA({
            State.Q0: Q0(),
            State.Q1: Q1(),
            State.Q2: Q2(),
            State.Q3: Q3(),
            State.Q4: Q4(),
        })

    def process(self, input_data: [int]):
        input_data = list(int_to_bool(val) for val in input_data)
        out = []
        current_state = self.instances[State.Q0]
        for input_datum in input_data:
            res = current_state.process(input_datum)
            out.append(res[1])
            current_state = self.instances[res[0]]
        res = list(bool_to_int(val) for val in out if val is not None)
        return res