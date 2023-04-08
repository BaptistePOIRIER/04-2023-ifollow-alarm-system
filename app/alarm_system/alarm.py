from alarm_type import AlarmType

class Alarm():
    def __init__(self, alarm_type: AlarmType, tick_rate: float) -> None:
        self.active = False

        self.priority = alarm_type.priority
        self.toggle_char = alarm_type.toggle_char
        self.beep_interval = alarm_type.beep_interval / tick_rate
        self.beep_duration = alarm_type.beep_duration / tick_rate
        self.beeps_before_pause = alarm_type.beeps_before_pause
        self.pause_duration = alarm_type.pause_duration / tick_rate

        self.color = alarm_type.color