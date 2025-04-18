import time

class CooldownTimer:
    def __init__(self, cooldown_time=1.0):
        self.cooldown_time = cooldown_time
        self.last_time = 0

    def ready(self):
        current_time = time.time()
        if current_time - self.last_time > self.cooldown_time:
            self.last_time = current_time
            return True
        return False
