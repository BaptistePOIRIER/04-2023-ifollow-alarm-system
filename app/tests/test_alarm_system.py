from src.alarm_system import AlarmSystem
from src.alarm import Alarm
from src.alarm_type import AlarmType


def test_alarm_system_init_default() -> None:
    alarm_system = AlarmSystem()

    assert alarm_system.tick_rate == 0.25

    alarm_low = Alarm(AlarmType.LOW, 0.25)
    alarm_medium = Alarm(AlarmType.MEDIUM, 0.25)
    alarm_high = Alarm(AlarmType.HIGH, 0.25)
    alarms = [alarm_low, alarm_medium, alarm_high]

    for i, alarm in enumerate(alarms):
        assert alarm == alarm_system.alarms[i]


def test_alarm_system_init() -> None:
    alarm_system = AlarmSystem(alarms=[AlarmType.LOW,AlarmType.HIGH], tick_rate=0.125)

    assert alarm_system.tick_rate == 0.125

    alarm_low = Alarm(AlarmType.LOW, 0.125)
    alarm_high = Alarm(AlarmType.HIGH, 0.125)
    alarms = [alarm_low, alarm_high]

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