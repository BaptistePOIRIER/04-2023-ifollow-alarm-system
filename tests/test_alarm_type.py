from app.alarm_type import AlarmType


def test_alarm_type_low() -> None:
    alarm = AlarmType.LOW

    assert alarm.priority == 1
    assert alarm.toggle_char == "l"
    assert alarm.beep_interval == 30
    assert alarm.beep_duration == 1
    assert alarm.beeps_before_pause == 1
    assert alarm.pause_duration == 0
    assert alarm.color == "\x1b[32m"


def test_alarm_type_medium() -> None:
    alarm = AlarmType.MEDIUM

    assert alarm.priority == 2
    assert alarm.toggle_char == "m"
    assert alarm.beep_interval == 1
    assert alarm.beep_duration == 0.25
    assert alarm.beeps_before_pause == 1
    assert alarm.pause_duration == 0
    assert alarm.color == "\x1b[33m"


def test_alarm_type_high() -> None:
    alarm = AlarmType.HIGH

    assert alarm.priority == 3
    assert alarm.toggle_char == "h"
    assert alarm.beep_interval == 0.5
    assert alarm.beep_duration == 0.25
    assert alarm.beeps_before_pause == 5
    assert alarm.pause_duration == 2
    assert alarm.color == "\x1b[31m"