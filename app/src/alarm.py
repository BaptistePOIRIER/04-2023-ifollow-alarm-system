from typing import Any

from src.alarm_type import AlarmType


class Alarm():
    def __init__(self, alarm_type: AlarmType, tick_rate: float) -> None:
        self.active = False

        self.name = alarm_type.name
        self.priority = alarm_type.priority
        self.toggle_char = alarm_type.toggle_char
        self.beep_interval = alarm_type.beep_interval / tick_rate
        self.beep_duration = alarm_type.beep_duration / tick_rate
        self.beeps_before_pause = alarm_type.beeps_before_pause
        self.pause_duration = alarm_type.pause_duration / tick_rate

        self.color = alarm_type.color
    

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Alarm):
            return False
        return (self.active == other.active and
                self.name == other.name and
                self.priority == other.priority and
                self.toggle_char == other.toggle_char and
                self.beep_interval == other.beep_interval and
                self.beep_duration == other.beep_duration and
                self.beeps_before_pause == other.beeps_before_pause and
                self.pause_duration == other.pause_duration and
                self.color == other.color)