import keyboard

from app.alarm_system import AlarmSystem
from app.alarm_type import AlarmType


def main():
    alarm_system = AlarmSystem()
    alarm_system.alarm_tick()
    
    keyboard.hook(alarm_system.key_event)

    try:
        while True:
            keyboard.wait()

    except KeyboardInterrupt:
        alarm_system.stop()


if __name__ == "__main__":
    main()