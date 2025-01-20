class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start

    def set_max(self, max_max):
        if max_max >= self.min_value:
            self.max_value = max_max

    def set_min(self, min_min):
        if min_min <= self.max_value:
            self.min_value = min_min

    def step_up(self):
        if self.current + 1 > self.max_value:
            raise ValueError("Достигнут максимум")
        self.current += 1

    def step_down(self):
        if self.current - 1 < self.min_value:
            raise ValueError("Достигнут минимум")
        self.current -= 1

    def get_current(self):
        return self.current


# Тесты
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, "Test1"

try:
    counter.step_up()
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, "Test2"

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, "Test3"

try:
    counter.step_down()
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, "Test4"
