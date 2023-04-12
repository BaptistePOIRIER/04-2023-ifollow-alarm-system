from unittest.mock import MagicMock, patch
import keyboard

from colorama import Fore, Style

from app.alarm_system import AlarmSystem
from app.alarm import Alarm
from app.alarm_type import AlarmType


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


def test_alarm_tick_no_beep(capsys) -> None:
    alarm_system = AlarmSystem()
    with patch("threading.Timer"):
        for _ in range(10):
            alarm_system.alarm_tick()

    captured = capsys.readouterr()
    assert captured.out == "".join([Style.RESET_ALL + "_" for _ in range(10)])

    

def test_alarm_tick_low_beep(capsys) -> None:
    alarm_system = AlarmSystem()
    alarm_system.toggle_alarm(alarm_system.alarms[0])
    with patch("threading.Timer"):
        for _ in range(240):
            alarm_system.alarm_tick()

    captured = capsys.readouterr()
    assert captured.out ==  "".join([Fore.GREEN + "X" for _ in range(4)]) + "".join([Fore.GREEN + "_" for _ in range(116)]) + \
                            "".join([Fore.GREEN + "X" for _ in range(4)]) + "".join([Fore.GREEN + "_" for _ in range(116)])
    

def test_alarm_tick_medium_beep(capsys) -> None:
    alarm_system = AlarmSystem()
    alarm_system.toggle_alarm(alarm_system.alarms[1])
    with patch("threading.Timer"):
        for _ in range(8):
            alarm_system.alarm_tick()

    captured = capsys.readouterr()
    assert captured.out ==  "".join([Fore.YELLOW + "X" for _ in range(1)]) + "".join([Fore.YELLOW + "_" for _ in range(3)]) + \
                            "".join([Fore.YELLOW + "X" for _ in range(1)]) + "".join([Fore.YELLOW + "_" for _ in range(3)])


def test_alarm_tick_high_beep(capsys) -> None:
    alarm_system = AlarmSystem()
    alarm_system.toggle_alarm(alarm_system.alarms[2])
    with patch("threading.Timer"):
        for _ in range(36):
            alarm_system.alarm_tick()

    captured = capsys.readouterr()
    assert captured.out ==  "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "_" for _ in range(8)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "X" for _ in range(1)]) + "".join([Fore.RED + "_" for _ in range(1)]) + \
                            "".join([Fore.RED + "_" for _ in range(8)])



def test_summarize_total_ticks() -> None:
    alarm_system = AlarmSystem()
    with patch("threading.Timer"):
        for _ in range(42):
            alarm_system.alarm_tick()
    assert alarm_system.summary["total_ticks"] == 42


def test_summarize_total_toggles() -> None:
    alarm_system = AlarmSystem()
    for _ in range(10):
        alarm_system.toggle_alarm(alarm_system.alarms[0])
    assert alarm_system.summary["total_toggles"] == 10


def test_summarize_print(capsys) -> None:
    alarm_system = AlarmSystem()
    
    alarm_system.toggle_alarm(alarm_system.alarms[0])
    alarm_system.summary["total_ticks"] = 42
    alarm_system.summary["total_toggles"] = 10

    alarm_system.summarize()

    captured = capsys.readouterr()
    assert captured.out == Fore.CYAN + f"\n\nElapsed time: {10.50:.2f} seconds ({42} characters printed)\n" + \
                           f"Alarms toggled: {10} times\n" + \
                           f"Alarms status: {['LOW: ON', 'MEDIUM: OFF', 'HIGH: OFF']}\n"
    

def test_stop() -> None:
    alarm_system = AlarmSystem()

    with patch("threading.Timer") as mock_timer:
        alarm_system.alarm_tick()
        alarm_system.stop()
        mock_timer.assert_called_with(alarm_system.tick_rate, alarm_system.alarm_tick)
        mock_timer.return_value.cancel.assert_called_once()