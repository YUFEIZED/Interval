class Interval:
    def __init__(self, min_val, max_val):
        if min_val > max_val:
            raise IntervalException('ERROR: the min_val must not be larger than max_val!')
        self.min_val = min_val
        self.max_val = max_val
        self.completed = False

    def complete(self):
        self.completed = True

    def __getattr__(self, key):
        if key == 'min_val':
            return self.min_val
        if key == 'max_val':
            return self.max_val
        if key == 'completed':
            return self.completed
        if key == 'format':
            return [self.min_val, self.max_val]


class IntervalException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)
