class LogException(Exception):
    def __init__(self):
        self.txt = 'negative!!!'


class TrigonometryException(Exception):
    def __init__(self):
        self.txt = 'invalid value'
