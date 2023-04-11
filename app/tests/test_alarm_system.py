from unittest.mock import MagicMock
import keyboard

from src.alarm_system import AlarmSystem
from src.alarm import Alarm
from src.alarm_type import AlarmType


def test_alarm_system_init_default() -> None:
    alarm_system = AlarmSystem()

    assert alarm_system.tick_rate == 0.25

    alarms = [Alarm(AlarmType.LOW, 0.25),
              Alarm(AlarmType.MEDIUM, 0.25),
              Alarm(AlarmType.HIGH, 0.25)]

    for i, alarm in enumerate(alarms):
        assert alarm == alarm_system.alarms[i]


def test_alarm_system_init() -> None:
    alarm_system = AlarmSystem(alarms=[AlarmType.LOW,AlarmType.HIGH], tick_rate=0.125)

    assert alarm_system.tick_rate == 0.125

    alarms = [Alarm(AlarmType.LOW, 0.125),
              Alarm(AlarmType.HIGH, 0.125)]

    for i, alarm in enumerate(alarms):
        assert alarm == alarm_system.alarms[i]


def test_toggle_alarm() -> None:
    alarm_system = AlarmSystem()

    alarm_system.toggle_alarm(alarm_system.alarms[0])
    assert alarm_system.alarms[0].active == True
    alarm_system.toggle_alarm(alarm_system.alarms[0])
    assert alarm_system.alarms[0].active == False

    alarm_system.toggle_alarm(alarm_system.alarms[0])
    assert alarm_system.current_alarm_priority == 1
    alarm_system.toggle_alarm(alarm_system.alarms[2])
    assert alarm_system.current_alarm_priority == 3
    alarm_system.toggle_alarm(alarm_system.alarms[1])
    assert alarm_system.current_alarm_priority == 3
    alarm_system.toggle_alarm(alarm_system.alarms[2])
    assert alarm_system.current_alarm_priority == 2
    alarm_system.toggle_alarm(alarm_system.alarms[1])
    alarm_system.toggle_alarm(alarm_system.alarms[0])
    assert alarm_system.current_alarm_priority == 0


def test_key_event() -> None:
    alarm_system = AlarmSystem()

    event = MagicMock(spec=keyboard._Event)
    event.name = "l"
    event.event_type = keyboard.KEY_DOWN

    alarm_system.key_event(event)
    assert alarm_system.alarms[0].active == True
    assert "l" in alarm_system.pressed_keys

    alarm_system.key_event(event)
    assert alarm_system.alarms[0].active == True
    assert "l" in alarm_system.pressed_keys

    event.event_type = keyboard.KEY_UP
    alarm_system.key_event(event)
    assert alarm_system.alarms[0].active == True
    assert "l" not in alarm_system.pressed_keys

    event.event_type = keyboard.KEY_DOWN
    alarm_system.key_event(event)
    assert alarm_system.alarms[0].active == False
    assert "l" in alarm_system.pressed_keys

    event.name = "a"
    alarm_system.key_event(event)
    assert alarm_system.alarms[0].active == False
    assert "a" not in alarm_system.pressed_keys