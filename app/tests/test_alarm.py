from colorama import Fore, Style

from src.alarm import Alarm
from src.alarm_type import AlarmType


def test_alarm_low_init() -> None:
    alarm = Alarm(AlarmType.LOW, 0.25)

    assert alarm.active == False
    assert alarm.name == "LOW"
    assert alarm.priority == 1
    assert alarm.toggle_char == "l"
    assert alarm.beep_interval == 120
    assert alarm.beep_duration == 4
    assert alarm.beeps_before_pause == 1
    assert alarm.pause_duration == 0
    assert alarm.color == Fore.GREEN


def test_alarm_medium_init() -> None:
    alarm = Alarm(AlarmType.MEDIUM, 0.25)

    assert alarm.active == False
    assert alarm.name == "MEDIUM"
    assert alarm.priority == 2
    assert alarm.toggle_char == "m"
    assert alarm.beep_interval == 4
    assert alarm.beep_duration == 1
    assert alarm.beeps_before_pause == 1
    assert alarm.pause_duration == 0
    assert alarm.color == Fore.YELLOW


def test_alarm_high_init() -> None:
    alarm = Alarm(AlarmType.HIGH, 0.25)

    assert alarm.active == False
    assert alarm.name == "HIGH"
    assert alarm.priority == 3
    assert alarm.toggle_char == "h"
    assert alarm.beep_interval == 2
    assert alarm.beep_duration == 1
    assert alarm.beeps_before_pause == 5
    assert alarm.pause_duration == 8
    assert alarm.color == Fore.RED


def test_alarm_eq() -> None:
    alarm1 = Alarm(AlarmType.LOW, 0.25)
    alarm2 = Alarm(AlarmType.LOW, 0.25)
    alarm3 = Alarm(AlarmType.MEDIUM, 0.25)

    assert alarm1 == alarm2
    assert alarm1 != alarm3
    assert alarm2 != alarm3
    assert alarm1 != "alarm"
    assert alarm2 != "alarm"
    assert alarm3 != "alarm"