from enum import Enum
from colorama import Fore, Style

class AlarmType(Enum):
    LOW = {"priority": 1, "toggle_char": "l", "beep_interval": 30, "beep_duration": 1, "color": Fore.GREEN}
    MEDIUM = {"priority": 2, "toggle_char": "m", "beep_interval": 1, "beep_duration": 0.25, "color": Fore.YELLOW}
    HIGH = {"priority": 3, "toggle_char": "h", "beep_interval": 0.5, "beep_duration": 0.25, "beeps_before_pause": 5, "pause_duration": 2, "color": Fore.RED}

    @property
    def priority(self):
        return self.value["priority"]

    @property
    def toggle_char(self):
        return self.value["toggle_char"]

    @property
    def beep_interval(self):
        return self.value["beep_interval"]

    @property
    def beep_duration(self):
        return self.value["beep_duration"]

    @property
    def beeps_before_pause(self):
        return self.value.get("beeps_before_pause", 1)

    @property
    def pause_duration(self):
        return self.value.get("pause_duration", 0)

    @property
    def color(self):
        return self.value.get("color", Style.RESET_ALL)