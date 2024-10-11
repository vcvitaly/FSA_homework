from enum import Enum

class State(Enum):
    Q0 = 0
    Q1 = 1
    Q2 = 2

class Q:
    def process(self, inpt: bool) -> State:
        pass

class Q0(Q):
    def process(self, inpt: bool) -> State:
        print(0)
        return State.Q1 if not inpt else State.Q0

class Q1(Q):
    def process(self, inpt: bool) -> State:
        if not (inpt):
            print(1)
            return State.Q2
        print(0)
        return State.Q0

class Q2(Q):
    def process(self, inpt: bool) -> State:
        print(0)
        return State.Q1 if not inpt else State.Q0

if __name__ == '__main__':
    input_data = list(map(lambda inpt: True if inpt == 1 else False, [1, 0, 1, 0, 0, 0, 0, 1, 1]))
    instances = {State.Q0: Q0(), State.Q1: Q1(), State.Q2: Q2()}
    currentState = instances[State.Q0]
    for input_datum in input_data:
        currentState = instances[currentState.process(input_datum)]
