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

        self.pressed_keys = set()

        self.alarms = [Alarm(alarm_type, self.tick_rate) for alarm_type in AlarmType]
        self.alarm: Alarm = None
        self.current_alarm_priority = 0

        self.alarm_tick()

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
        self.timer = threading.Timer(self.tick_rate, self.alarm_tick)
        self.timer.start()

    def key_event(self, event):
        key_name = event.name

        for alarm in self.alarms:
            if key_name == alarm.toggle_char and event.event_type == keyboard.KEY_DOWN:
                if key_name not in self.pressed_keys:
                    self.toggle_alarm(alarm)
                    self.pressed_keys.add(key_name)
            
            elif event.event_type == keyboard.KEY_UP:
                if key_name in self.pressed_keys:
                    self.pressed_keys.remove(key_name)

    def run(self) -> None:
        keyboard.hook(self.key_event)
        keyboard.wait('ctrl+c')

        self.timer.cancel()
        print(Fore.CYAN + "\n\nResults:")

if __name__ == "__main__":
    AlarmSystem().run()