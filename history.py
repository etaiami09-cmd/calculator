from copy import deepcopy
class Tracker():
    def __init__(self):
        self.calculations = []
    def add_calculation(self, calculation):
        self.calculations.append(calculation)
        if len(self.calculations) > 10:
            self.calculations.pop(0)
    def calculations_by_recent(self):
        return deepcopy(self.calculations)[::-1]