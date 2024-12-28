class LapTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_lap(self):
        from time import time
        self.start_time = time()

    def end_lap(self):
        from time import time
        self.end_time = time()

    @property
    def lap_time(self):
        if self.start_time is None or self.end_time is None:
            return None
        return self.end_time - self.start_time