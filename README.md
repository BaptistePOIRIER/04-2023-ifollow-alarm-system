# iFollow Test : Alarm System

The purpose of this repo is for [iFollow](https://ifollow.fr)'s technical team, to be able to review my technical abilities facing the following [instructions](ifollow_test.pdf).

## Table of contents
  - [Installation](#installation)
  - [Usage](#usage)
  - [Tests](#tests)
  - [How it works](#how-it-works)
    - [AlarmType](#alarmtype)
    - [Alarm](#alarm)
    - [AlarmSystem](#alarmsystem)
  - [Main](#main)
  - [License](#license)

## Installation

After cloning the repository, use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements. In a terminal, navigate to the root directory and run the following command:

```bash
pip install .
```

Expected output:

![Expected output](https://user-images.githubusercontent.com/75702738/231614151-43ad89a1-3301-4cc5-838d-32c7882f7d8d.png)

## Usage

To run the alarm system, navigate to the root directory and run the following command:

```bash
python main.py
```

Demo:

![Demo](https://user-images.githubusercontent.com/75702738/231619335-2ab08174-c2f2-4916-b786-74f2576ceb4a.gif)


## Tests

To run the tests, navigate to the root directory and run the following command:

```bash
python setup.py test
```

Expected output:

![Expected output](https://user-images.githubusercontent.com/75702738/231615265-632d8ed9-bb9f-49b3-8498-91dd808767d1.png)


## How it works

The alarm system is composed of 3 main classes dividing the app in smaller parts, to make it more readable and maintainable:
### AlarmType
This class is an enum that contains the different types of alarms that can be triggered by the system. It makes it easy to add, remove or modify the different types of alarms, specifying the following attributes in a dictionnary:

| Attribute | Description |
| --- | --- |
| `priority` | Priority of the alarm |
| `toggle_char` | Keyboard key used to toggle the alarm |
| `beep_interval` | Period of a full beep cycle *(in seconds)* |
| `beep_duration` | Duration of a beep *(in seconds)* |
| `beeps_before_pause` | Amount of beeps before a pause *(default=1)* |
| `pause_duration` | Duration of a pause *(default=0)* |
| `color` | Alarm displayed color *(default=default system color)* |

### Alarm
This class creates the alarm objects, being given an `AlarmType` and a `tick_rate`. It reads the *AlarmType* attibutes and converts the timings in ticks using the *tick_rate* value. It also defines an `active` boolean attibute to define weather the alarm is active or not, and that's it's main purpose *(considering that the other computations could have been done in the AlarmSystem itself, but were made here so they are only computed once)*.

### AlarmSystem
This class is the main class of the system. It creates the alarm system, being given a list of `AlarmType` and a `tick_rate`. It defines a list of all the alarms objects, created using the `Alarm` class, which will be used to manage the alarms. The *tick_rate* purpose is to have a more maintainable code if some alarms required using some different timings in the future. This class defines the following methods:

- `toggle_alarm`: Called given an alarm object, it toggles its active state. It also changes the current alarm if the newly activated alarm has a higher priority or if the current alarm is not active anymore.

- `key_event`: Called by a keyboard event, it handles the keys inputs to toggle the alarms. It uses a collection of keys to prevent alarms from triggering multiple times if the triggering is hold.

- `alarm_tick`: Called every tick by a timer, it prints the state of the current alarm, simulating a beep or a no beep.

- `summarize`: Called by the *stop()* method, it prints some summary information, that were counted throughout the app execution.

- `stop`: Called by the *main.py* file, it stops the app by stopping the tickign timer and printing the summary information.

## Main
Finally, the `main.py` file is the main file of the app. It creates the alarm system, starts the alarm tick loop which update the alarms every tick. It also handles the keyboard inputs to toggle the alarms and stop the app.

## License
This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details.