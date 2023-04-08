import keyboard
import threading
import time

from colorama import Fore, Style, init

from alarm_type import AlarmType
from alarm import Alarm

init()

class AlarmSystem:
    def __init__(self) -> None:
        self.tick_rate = 0.25
        self.tick = 0

        self.alarms = [Alarm(alarm_type, self.tick_rate) for alarm_type in AlarmType]
        self.alarm: Alarm = None
        self.current_alarm_priority = 0

        self.timer = threading.Timer(self.tick_rate, self.alarm_tick).start()

    def toggle_alarm(self, alarm: Alarm) -> None:
        alarm.active = not alarm.active

        old_alarm_priority = self.current_alarm_priority
        self.current_alarm_priority = max([alarm.priority for alarm in self.alarms if alarm.active], default=0)

        if self.current_alarm_priority != 0 and self.current_alarm_priority != old_alarm_priority:
            self.alarm = max([alarm for alarm in self.alarms if alarm.active], key=lambda alarm: alarm.priority)
            self.tick = 0

    def alarm_tick(self) -> None:
        if self.current_alarm_priority != 0:
            if (self.tick % self.alarm.beep_interval < self.alarm.beep_duration and
                self.tick % (self.alarm.beeps_before_pause*self.alarm.beep_interval + self.alarm.pause_duration) < self.alarm.beeps_before_pause*self.alarm.beep_interval):
                print(self.alarm.color + "X", end="")
            else:
                print(self.alarm.color + "_", end="")
        else:
            print(Style.RESET_ALL + "_", end="")

        self.tick += 1
        threading.Timer(self.tick_rate, self.alarm_tick).start()

    def run(self) -> None:
        while True:
            for alarm in self.alarms:
                if keyboard.is_pressed(alarm.toggle_char):
                    self.toggle_alarm(alarm)
                    time.sleep(0.5)

if __name__ == "__main__":
    AlarmSystem().run()