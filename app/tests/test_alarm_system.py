import unittest
from unittest.mock import Mock
from alarm_system import AlarmSystem

class TestAlarmSystem(unittest.TestCase):

    def test_toggle_alarm(self):
        alarm_system = AlarmSystem()
        alarm = alarm_system.alarms[0]

        initial_state = alarm.active
        initial_total_toggles = alarm_system.summary["total_toggles"]

        alarm_system.toggle_alarm(alarm)

        self.assertEqual(alarm.active, not initial_state)
        self.assertEqual(alarm_system.summary["total_toggles"], initial_total_toggles + 1)

    def test_key_event(self):
        alarm_system = AlarmSystem()
        alarm = alarm_system.alarms[0]

        initial_state = alarm.active

        mock_key_down_event = Mock(name=alarm.toggle_char, event_type='down')
        mock_key_up_event = Mock(name=alarm.toggle_char, event_type='up')

        alarm_system.key_event(mock_key_down_event)

        self.assertEqual(alarm.active, not initial_state)
        self.assertIn(alarm.toggle_char, alarm_system.pressed_keys)

        alarm_system.key_event(mock_key_up_event)

        self.assertNotIn(alarm.toggle_char, alarm_system.pressed_keys)

if __name__ == "__main__":
    unittest.main()
